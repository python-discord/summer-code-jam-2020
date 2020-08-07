from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=50, default="Room")
    description = models.TextField(max_length=512)
    connections = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
