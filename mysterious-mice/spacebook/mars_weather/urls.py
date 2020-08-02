from django.urls import path
from .views import CurrentWeatherView

urlpatterns = [
    path("weather/current/", CurrentWeatherView.as_view(), name="current_weather"),
]
