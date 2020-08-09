from django.urls import path
from .views import index, about_us

app_name = "home"
urlpatterns = [
    path("", index, name="index"),
    path("about-us/", about_us, name="about-us"),
]

handler404 = 'home.views.error_404_view'
