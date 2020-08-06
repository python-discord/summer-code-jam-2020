from django.urls import path, include
from .views import homepage, aboutus

urlpatterns = [
    path("", homepage, name="homepage"),
    path("aboutus", aboutus, name="aboutus"),
]
