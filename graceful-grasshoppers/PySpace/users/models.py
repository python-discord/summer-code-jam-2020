from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """The user model"""
    name = models.CharField(blank=True, max_length=255)
    about = models.TextField(default='...', blank=True, max_length=255)
    age = models.IntegerField(default=14)

    def __str__(self):
        return self.email


class Friendship(models.Model):
    """Describes a friendship between two users"""
    requester = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="following", default=None)
    friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="followers", default=None)
    friends = []
    pending = models.BooleanField(default=True)
