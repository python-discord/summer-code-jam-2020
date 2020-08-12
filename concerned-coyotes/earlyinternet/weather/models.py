from django.db import models
from django.utils import timezone


class WeatherManager(models.Manager):

    def get_weather_at(self, lat, lon):
        return super().get_queryset().filter(
            latitude=lat, longitude=lon,
            day=timezone.now()
        ).order_by("-day").first()


class Weather(models.Model):

    objects = WeatherManager()

    celsius = models.FloatField()
    fahrenheit = models.FloatField()
    city = models.CharField(max_length=512)
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    day = models.DateField(default=timezone.now)
    latitude = models.FloatField()
    longitude = models.FloatField()
