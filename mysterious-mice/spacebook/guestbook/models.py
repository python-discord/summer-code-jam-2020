from django.conf import settings
from django.db import models
from django.utils import timezone


class Guestbook(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    published_date = models.DateTimeField(blank=True, null=True)


