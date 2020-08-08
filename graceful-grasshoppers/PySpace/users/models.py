from django.contrib.auth.models import AbstractUser
from django.db import models
import post.models as post_models


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


class ProfileComment(models.Model):

    content = models.TextField()
    user_commented_on = models.ForeignKey(CustomUser, models.CASCADE)
    user_commented = models.ForeignKey(CustomUser, models.CASCADE)

    def __str__(self):  # Returns a short intro of 20 words
        return " ".join(self.content.split(" ")[:20])


