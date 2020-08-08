from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude = models.FloatField()
