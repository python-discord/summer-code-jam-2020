from django.contrib.auth.models import User

from .models import Weather
from .utils import get_weather


def update_weather_for_user(user: User) -> None:
    location = user.location_set.last()
    lat = location.latitude
    lon = location.longitude

    weather = get_weather(lat, lon)

    # create weather objects
    Weather.objects.create(
        celsius=weather['weather']['celsius'],
        fahrenheit=weather['weather']['fahrenheit'],
        city=weather['city'],
        sunrise=weather['sunrise'],
        sunset=weather['sunset'],
        day=weather['date'],
        latitude=lat,
        longitude=lon,
    )


def fetch_weather() -> None:
    for user in User.objects.all():
        if user.location_set.exists():
            update_weather_for_user(user)
