from django.contrib.auth.views import LoginView
from django.urls import path

from . import views


urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("login/", LoginView.as_view(), name='login'),
    path("signup/", views.signup, name="signup"),
]
