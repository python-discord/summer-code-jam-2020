from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)


class Room(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    description = models.CharField(max_length=512)
