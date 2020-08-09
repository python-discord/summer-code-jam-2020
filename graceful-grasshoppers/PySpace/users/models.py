from django.contrib.auth.models import AbstractUser
from django.db import models
from api.models import File


def default_profile_picture():
    return File.objects.get(file='default_profile.jpg').id


class CustomUser(AbstractUser):
    """The user model"""
    name = models.CharField(blank=True, max_length=255)
    about = models.TextField(default='...', blank=True, max_length=255)
    age = models.IntegerField(default=14)
    profile_picture = models.ForeignKey(File, on_delete=models.CASCADE, default=default_profile_picture)

    def __str__(self):
        return self.email


class Friendship(models.Model):
    """Describes a friendship between two users"""
    requester = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="following", default=None)
    friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="followers", default=None)
    friends = []
    pending = models.BooleanField(default=False)


class ProfileComment(models.Model):
    """A comment on a user's profile"""
    content = models.TextField()
    user_commented_on = models.ForeignKey(CustomUser, models.CASCADE, related_name="user_commented")
    user_commented = models.ForeignKey(CustomUser, models.CASCADE, related_name="user_profile_commented_on")

    def __str__(self):  # Returns a short intro of 20 words
        return " ".join(self.content.split()[:20])
