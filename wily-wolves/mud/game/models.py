"""The game models."""
from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    """The player representation for a user."""

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.BigIntegerField(default=0)
    max_health = models.BigIntegerField(default=100)
    current_health = models.BigIntegerField(default=100)
    experience = models.BigIntegerField(default=0)
