from django.db import models


class Weather(models.Model):

    celsius = models.FloatField()
    fahrenheit = models.FloatField()
    city = models.CharField(max_length=512)
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
