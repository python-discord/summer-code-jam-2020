from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class DiaryEntry(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.title} -- {self.content[:50]}'
