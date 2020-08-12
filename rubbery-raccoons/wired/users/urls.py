from django.contrib.auth import views as auth_views
from django.urls import path

from . import views as users_views

urlpatterns = [
    path("register", users_views.register, name="register"),
    path(
        "login", auth_views.LoginView.as_view(template_name="users/login.html"), name="login_view"
    ),
    path("logout", users_views.logout_view, name="logout_view"),
]
