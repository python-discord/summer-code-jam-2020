"""The game models."""
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    """A game location object."""

    x_coord = models.BigIntegerField(default=0, null=False)
    y_coord = models.BigIntegerField(default=0, null=False)
    z_coord = models.BigIntegerField(default=0, null=False)
    description = models.TextField()


class NPC(models.Model):
    """A representation for NPCs."""

    class NPCTypes(models.TextChoices):
        MERCHANT = 'MC', _('Merchant')
        ENEMY = 'EN', _('Enemy')
        CIVILIAN = 'CV', _('Civilian')

    name = models.TextField()
    max_health = models.BigIntegerField(default=100)
    current_health = models.BigIntegerField(default=100)
    npc_type = models.CharField(max_length=2, choices=NPCTypes.choices, default=NPCTypes.ENEMY)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)


class Player(models.Model):
    """The player representation for a user."""

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.BigIntegerField(default=0)
    max_health = models.BigIntegerField(default=100)
    current_health = models.BigIntegerField(default=100)
    experience = models.BigIntegerField(default=0)
    location_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
