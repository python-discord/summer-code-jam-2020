from django.urls import path
from .views import Welcome

app_name = "welcome_page"
urlpatterns = [
    path("", Welcome.as_view(), name="welcome_page"),
]
