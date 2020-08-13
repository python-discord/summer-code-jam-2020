from django.db import models
from django.utils import timezone

from shiny_sheep.users.models import User


class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_room',
                              null=True, blank=True)  # null if system created the room
    date_created = models.DateTimeField(default=timezone.now)
    users = models.ManyToManyField(User, related_name='room')

    def __str__(self):
        return self.name
