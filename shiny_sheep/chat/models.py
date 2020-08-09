from django.db import models
from django.utils import timezone

from shiny_sheep.users.models import User


class Room(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              null=True, blank=True)  # null if system created the room
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
