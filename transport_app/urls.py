from django.urls import path
from . import views

urlpatterns = [
    # General Navigation
    path("", views.home, name="home"),
    path("schedule/", views.schedule_view, name="schedule"),
    path("staff-info/", views.staff_info_view, name="staff_info"),
    # Authentication
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout_user"),
    # User Profile & Transport Card
    path("profile/", views.profile_view, name="profile"),
    path("view-card/", views.generate_card_view, name="generate_card"),
    # Administrative Views
    path("admin-users/", views.view_registered_users, name="admin_users"),
]
