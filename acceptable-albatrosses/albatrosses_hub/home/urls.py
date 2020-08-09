from django.urls import path, include
from .views import homepage, about_us

urlpatterns = [
    path("", homepage, name="homepage"),
    path("about-us/", about_us, name="about_us"),
]

handler404 = 'home.views.error_404_view'
