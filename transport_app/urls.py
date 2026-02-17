from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Navigation
    path("", views.home, name="home"),
    path("schedule/updates/", views.schedule_view, name="schedule"),
    path("schedule/central/", views.central_schedule_view, name="central_schedule"),
    path("staff-info/", views.staff_info_view, name="staff_info"),
    # Information & Legal
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("terms/", views.terms_view, name="terms"),
    path("privacy/", views.privacy_view, name="privacy"),
    path("disclaimer/", views.disclaimer_view, name="disclaimer"),
    # Authentication
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout_user"),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="transport_app/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="transport_app/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    # User Profile
    path("profile/", views.profile_view, name="profile"),
    path("view-card/", views.generate_card_view, name="generate_card"),
    # Admin & Export
    path("admin-users/", views.admin_users_view, name="admin_users"),
    path("schedule/post/", views.post_schedule_view, name="post_schedule"),
    path("schedule/export/", views.export_schedule_pdf, name="export_pdf"),
]
