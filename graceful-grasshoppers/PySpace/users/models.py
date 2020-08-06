from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    friends = []
    friend_requests_pending = []
    friend_requests_sent = []

    def __str__(self):
        return self.email
