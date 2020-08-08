from django.db import models
from django.contrib.auth.models import User


class Messages(models.Model):
    message = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recipent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipent')
