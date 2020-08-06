from django.urls import path, include
from .views import register_page, login_page, logout_page


urlpatterns = [
    path("register/", register_page, name="register_page"),
    path("login/", login_page, name="login_page"),
    path("logout/", logout_page, name="logout_page")
]
