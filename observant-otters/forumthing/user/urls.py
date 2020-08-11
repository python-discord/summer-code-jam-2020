from django.urls import path
from . import views

urlpatterns = [
    path('profile/',
         views.profile,
         name='profile'),
    path(
        "login/",
        views.Login.as_view(),
        name="login"
    ),
    path(
        "logout/",
        views.Logout.as_view(),
        name="logout"
    ),
    path("register/",
         views.register,
         name="register")
]
