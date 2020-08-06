from django.contrib.auth.models import AbstractUser
from django.db import models


class ProfileComment(models.Model):

    content = models.TextField()

    def __str__(self):  # Returns a short intro of 20 words
        return " ".join(self.content.split(" ")[:20])


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    friends = []
    friend_requests_pending = []
    friend_requests_sent = []
    comments = models.ManyToManyField(ProfileComment)

    def __str__(self):
        return self.email
