from django.urls import path, include
from .views import register_page


urlpatterns = [
    path("register/", register_page, name="register_page")
]
