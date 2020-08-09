from django.db import models
from django.contrib.auth.models import AbstractUser


class ForumUser(AbstractUser):
    username = models.CharField(unique=True, max_length=50)
    nickname = models.CharField(default='', max_length=50)
    email = models.EmailField(default='none@smth.com')

    def __str__(self):  # maybe a better string repr?
        if self.nickname:
            return self.nickname
        return self.username
