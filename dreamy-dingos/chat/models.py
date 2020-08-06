from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SimpleUser(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=50)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
