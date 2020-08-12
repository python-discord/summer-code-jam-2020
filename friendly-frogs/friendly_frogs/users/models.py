from django.db import models
from django.contrib.auth.models import User

choices = (('bbc-news', "BBC-NEWS"),)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    news_source = models.CharField(
        max_length=50, default='bbc-news', choices=choices)

    def __str__(self):
        return f"{self.user.username} profile"
