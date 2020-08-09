from django.contrib.auth.models import User

from .models import Weather
from .utils import get_weather


def fetch_weather():
    for user in User.objects.all():
        lat, lon = user.location_set
        weather = get_weather(lat, lon)
        # create weather objects
        Weather.objects.create(
            celsius=weather['weather']['celsius'],
            fahrenheit=weather['weather']['fahrenheit'],
            city=weather['city'],
            sunrise=weather['sunrise'],
            sunset=weather['sunset'],
            day=weather['day'],
            latitude=lat,
            longitude=lon
        )
