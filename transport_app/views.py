from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Card, Schedule


def home(request):
    return render(request, "transport_app/home.html")


def register_view(request):
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

        if (
            User.objects.filter(email=email).exists()
            or User.objects.filter(id_number=id_number).exists()
        ):
            messages.error(request, "User already exists with this email or ID.")
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
            messages.success(request, "Success! Please login.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
    return render(request, "transport_app/register.html")


def login_view(request):
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
    staff_members = User.objects.filter(role__in=["staff", "faculty"])
    return render(
        request, "transport_app/staff_info.html", {"staff_members": staff_members}
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
        messages.success(request, "Logged out.")
        return redirect("login")
    return redirect("home")
