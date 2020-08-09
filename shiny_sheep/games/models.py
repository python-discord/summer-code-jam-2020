from django.db import models

from shiny_sheep.users.models import User


class Room(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              null=True, blank=True)  # null if system created the room
    average_rating = models.IntegerField(null=True, blank=True)
    game_type = models.CharField(max_length=50)
    game_id = models.IntegerField(null=True, blank=True, unique=True)
