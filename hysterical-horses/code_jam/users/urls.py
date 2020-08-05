from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("login/", LoginView.as_view(template_name='users/login.html',
         redirect_authenticated_user=True), name='login'),
    path("logout/", LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),
    path("signup/", views.signup, name="signup"),
]
