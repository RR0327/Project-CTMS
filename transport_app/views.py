import io
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse
from django.core.mail import send_mail
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .models import User, Card, Schedule
import re

# --- Public Views ---


def home(request):
    """Renders the landing page with animations."""
    return render(request, "transport_app/home.html")


def central_schedule_view(request):
    """Public view for the central schedule with trip-type filtering."""
    schedules = Schedule.objects.all().order_by("-date", "-time")
    return render(
        request, "transport_app/central-schedule.html", {"schedules": schedules}
    )


def about_view(request):
    """Information about BAIUST transport."""
    return render(request, "transport_app/about.html")


def contact_view(request):
    """Handles contact form submissions and sends emails to admin."""
    if request.method == "POST":
        name = request.POST.get("name")
        sender_email = request.POST.get("email")
        message = request.POST.get("message")

        try:
            send_mail(
                f"CTMS Contact from {name}",
                message,
                sender_email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, "Email service error. Please try again later.")
        return redirect("contact")
    return render(request, "transport_app/contact.html")


def terms_view(request):
    """Legal terms for transport usage."""
    return render(request, "transport_app/terms.html")


def privacy_view(request):
    """Data privacy policy."""
    return render(request, "transport_app/privacy.html")


def disclaimer_view(request):
    """Service disclaimers."""
    return render(request, "transport_app/disclaimer.html")


# --- Authentication ---


def register_view(request):
    """Handles user registration and auto-generates a card."""
    if request.method == "POST":
        data = request.POST
        # Validate and normalize Bangladeshi mobile numbers.
        contact_raw = data.get("contact_information", "").strip()
        # Remove non-digit characters
        contact_digits = re.sub(r"\D", "", contact_raw)
        # Expect local format: 01xxxxxxxxx (11 digits)
        if not re.fullmatch(r"01\d{9}", contact_digits):
            messages.error(request, "Contact number must be 11 digits and start with '01'.")
            return render(request, "transport_app/register.html")

        # Normalize to international format +8801xxxxxxxxx (drop leading 0)
        contact_normalized = "+880" + contact_digits[1:]

        try:
            user = User.objects.create_user(
                email=data.get("email"),
                name=data.get("name"),
                role=data.get("role"),
                id_number=data.get("id_number"),
                level=data.get("level"),
                term=data.get("term"),
                contact_information=contact_normalized,
                password=data.get("password"),
            )
            Card.objects.create(user=user)
            messages.success(request, "Account created! You can now login.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
    return render(request, "transport_app/register.html")


def login_view(request):
    """Authenticates users."""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect("profile")
        messages.error(request, "Invalid email or password.")
    return render(request, "transport_app/login.html")


def logout_view(request):
    """Logs out users."""
    if request.method == "POST":
        logout(request)
        return redirect("home")
    return redirect("home")


# --- Protected User Views ---


@login_required
def profile_view(request):
    """User profile and transport card details."""
    card = getattr(request.user, "card", None)
    return render(
        request, "transport_app/profile.html", {"user": request.user, "card": card}
    )


@login_required
def generate_card_view(request):
    """Generates the digital transport pass."""
    card, _ = Card.objects.get_or_create(user=request.user)
    return render(
        request,
        "transport_app/card_generation.html",
        {"user": request.user, "card": card},
    )


@login_required
def schedule_view(request):
    """Card-based 'Latest Updates' view."""
    schedules = Schedule.objects.all().order_by("-updated_at")
    return render(request, "transport_app/schedule.html", {"schedules": schedules})


@login_required
def staff_info_view(request):
    """Lists staff/faculty. Uses staff-info.html."""
    staff_members = User.objects.filter(role__in=["staff", "faculty"])
    return render(
        request, "transport_app/staff-info.html", {"staff_members": staff_members}
    )


# --- Administrative Views ---


@login_required
def admin_users_view(request):
    """Dashboard to manage registered users."""
    if not request.user.is_admin:
        return redirect("home")
    users = User.objects.all()
    return render(request, "transport_app/admin_users.html", {"users": users})


@login_required
def post_schedule_view(request):
    """Form for admins to post new trips."""
    if not request.user.is_admin:
        return redirect("home")
    if request.method == "POST":
        Schedule.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            date=request.POST.get("date"),
            time=request.POST.get("time"),
            trip_type=request.POST.get("trip_type"),
        )
        messages.success(request, "Schedule published!")
        return redirect("central_schedule")
    return render(request, "transport_app/post-schedule.html")


@login_required
def export_schedule_pdf(request):
    """Generates a PDF download of all schedules."""
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, "BAIUST Central Transport Schedule")
    p.setFont("Helvetica", 10)
    y = 700
    for s in Schedule.objects.all():
        p.drawString(
            100, y, f"{s.get_trip_type_display()} | {s.title} | {s.date} | {s.time}"
        )
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="Schedule.pdf")
