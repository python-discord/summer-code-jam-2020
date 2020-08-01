from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Thread(models.Model):
    start_date = models.DateTimeField('Date created', auto_now_add=True)
    title = models.CharField(max_length=120)


class ThreadMessage(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET("Deleted"))
    date = models.DateTimeField('Date created', auto_now_add=True)
    message = models.TextField()
