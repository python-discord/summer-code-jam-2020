from django.conf import settings
from django.db import models
from django.utils import timezone


class Guestbook(models.Model):
    author = models.TextField()
    text = models.TextField()
    email = models.EmailField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
