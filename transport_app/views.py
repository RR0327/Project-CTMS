from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Card, Schedule


def home(request):
    """Renders the home page."""
    return render(request, "transport_app/home.html")


def register_view(request):
    """Handles user registration and automatically creates a Transport Card."""
    if request.method == "POST":
        data = request.POST
        name = data.get("name").strip()
        email = data.get("email").strip()
        role = data.get("role")
        password = data.get("password")
        id_number = data.get("id_number").strip()
        level = data.get("level") if role == "student" else None
        term = data.get("term") if role == "student" else None
        contact_information = data.get("contact_information").strip()

        # Validation logic
        if not all([name, email, role, password, id_number, contact_information]):
            messages.error(request, "All fields are required.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return redirect("register")

        if User.objects.filter(id_number=id_number).exists():
            messages.error(request, "This ID number is already registered.")
            return redirect("register")

        try:
            # Create user in SQLite
            user = User.objects.create_user(
                email=email,
                name=name,
                role=role,
                id_number=id_number,
                level=level,
                term=term,
                contact_information=contact_information,
                password=password,
            )
            # Automatically trigger Card/QR generation via the model
            Card.objects.create(user=user)
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Error during registration: {str(e)}")
            return redirect("register")

    return render(request, "transport_app/register.html")


def login_view(request):
    """Handles user authentication."""
    if request.method == "POST":
        email = request.POST.get("email").strip()
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("profile")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect("login")

    return render(request, "transport_app/login.html")


@login_required
def profile_view(request):
    """Displays user profile and their associated transport card."""
    user = request.user
    card = getattr(user, "card", None)
    return render(request, "transport_app/profile.html", {"user": user, "card": card})


@login_required
def generate_card_view(request):
    """Displays the printable card page using the stored QR code."""
    user = request.user
    # Ensure a card exists; if not, create one
    card, created = Card.objects.get_or_create(user=user)
    return render(
        request, "transport_app/card_generation.html", {"user": user, "card": card}
    )


@login_required
def schedule_view(request):
    """Lists all transport schedules ordered by the latest update."""
    schedules = Schedule.objects.all().order_by("-updated_at")
    return render(request, "transport_app/schedule.html", {"schedules": schedules})


def staff_info_view(request):
    """Public view to see staff and faculty contact details."""
    staff_members = User.objects.filter(role__in=["staff", "faculty"])
    return render(
        request, "transport_app/staff_info.html", {"staff_members": staff_members}
    )


@login_required
def view_registered_users(request):
    """Admin-only view to see a list of all registered users."""
    if not request.user.is_admin:
        messages.error(request, "Access denied.")
        return redirect("home")
    users = User.objects.all()
    return render(request, "transport_app/admin_users.html", {"users": users})


def logout_view(request):
    """Logs the user out safely."""
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect("login")
    return redirect("home")
