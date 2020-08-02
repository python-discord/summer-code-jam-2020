from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    z = models.IntegerField(default=0)


class Room(models.Model):
    description = models.CharField(max_length=512)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    z = models.IntegerField(default=0)
