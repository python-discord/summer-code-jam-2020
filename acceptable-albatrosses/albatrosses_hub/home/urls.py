from django.urls import path, include
from .views import homepage

urlpatterns = [
    path("", homepage, name="homepage")
]
