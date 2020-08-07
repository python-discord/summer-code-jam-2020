from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    friends = []
    friend_requests_pending = []
    friend_requests_sent = []

    def __str__(self):
        return self.email


class ProfileComment(models.Model):

    content = models.TextField()
    user_commented_on = models.ForeignKey(CustomUser, models.CASCADE)
    user_commented = models.ForeignKey(CustomUser, models.CASCADE)

    def __str__(self):  # Returns a short intro of 20 words
        return " ".join(self.content.split(" ")[:20])
