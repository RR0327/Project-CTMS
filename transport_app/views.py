from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Card, Schedule


def home(request):
    """Renders the home page with dynamic button logic."""
    return render(request, "transport_app/home.html")


def register_view(request):
    """Handles user registration and creates a Transport Card."""
    if request.method == "POST":
        data = request.POST
        name, email, role = (
            data.get("name").strip(),
            data.get("email").strip(),
            data.get("role"),
        )
        password, id_number = data.get("password"), data.get("id_number").strip()
        contact_info = data.get("contact_information").strip()
        level = data.get("level") if role == "student" else None
        term = data.get("term") if role == "student" else None

        if not all([name, email, role, password, id_number, contact_info]):
            messages.error(request, "All fields are required.")
            return redirect("register")

        try:
            user = User.objects.create_user(
                email=email,
                name=name,
                role=role,
                id_number=id_number,
                level=level,
                term=term,
                contact_information=contact_info,
                password=password,
            )
            Card.objects.create(user=user)
            messages.success(request, "Registration successful! Please login.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
    return render(request, "transport_app/register.html")


def login_view(request):
    """Handles user authentication."""
    if request.method == "POST":
        email, pw = request.POST.get("email").strip(), request.POST.get("password")
        user = authenticate(request, email=email, password=pw)
        if user:
            login(request, user)
            return redirect("profile")
        messages.error(request, "Invalid credentials.")
    return render(request, "transport_app/login.html")


@login_required
def profile_view(request):
    card = getattr(request.user, "card", None)
    return render(
        request, "transport_app/profile.html", {"user": request.user, "card": card}
    )


@login_required
def generate_card_view(request):
    card, _ = Card.objects.get_or_create(user=request.user)
    return render(
        request,
        "transport_app/card_generation.html",
        {"user": request.user, "card": card},
    )


@login_required
def schedule_view(request):
    schedules = Schedule.objects.all().order_by("-updated_at")
    return render(request, "transport_app/schedule.html", {"schedules": schedules})


def staff_info_view(request):
    """FIX: Points to staff-info.html to match your file directory naming."""
    staff_members = User.objects.filter(role__in=["staff", "faculty"])
    return render(
        request, "transport_app/staff-info.html", {"staff_members": staff_members}
    )


@login_required
def view_registered_users(request):
    if not request.user.is_admin:
        return redirect("home")
    return render(
        request, "transport_app/admin_users.html", {"users": User.objects.all()}
    )


def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Logged out successfully.")
        return redirect("login")
    return redirect("home")


@login_required
def central_schedule_view(request):
    """
    Renders the new Central Transport Schedule using the table layout.
    """
    schedules = Schedule.objects.all().order_by("-updated_at")
    return render(
        request, "transport_app/central_schedule.html", {"schedules": schedules}
    )


@login_required
def admin_users_view(request):
    """
    A protected dashboard view to list all registered users for administrators.
    """
    if not request.user.is_admin:
        return redirect("home")

    users = User.objects.all().order_by("role", "name")
    return render(request, "transport_app/admin_users.html", {"users": users})


@login_required
def staff_info_view(request):
    """
    Lists all staff and faculty. Fixed to point to staff-info.html.
    """
    staff_members = User.objects.filter(role__in=["staff", "faculty"]).order_by("name")
    return render(
        request, "transport_app/staff-info.html", {"staff_members": staff_members}
    )


def central_schedule_view(request):
    schedules = Schedule.objects.all().order_by("-date", "-time")
    # This string must match the filename in your templates folder exactly
    return render(
        request, "transport_app/central-schedule.html", {"schedules": schedules}
    )


@login_required
def post_schedule_view(request):
    if not request.user.is_admin:
        messages.error(request, "Admin privileges required.")
        return redirect("home")

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = request.POST.get("date")
        time = request.POST.get("time")
        trip_type = request.POST.get("trip_type")  # Capture trip type

        if all([title, date, time, trip_type]):
            Schedule.objects.create(
                title=title,
                description=description,
                date=date,
                time=time,
                trip_type=trip_type,
            )
            messages.success(request, "Schedule posted successfully!")
            return redirect("central_schedule")

    return render(request, "transport_app/post-schedule.html")
