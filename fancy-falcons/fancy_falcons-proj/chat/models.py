from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sender',
    )
    reciever = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reciever',
    )
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'From {self.sender} to {self.reciever} at {self.date}'