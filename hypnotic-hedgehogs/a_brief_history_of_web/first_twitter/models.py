from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    date_posted = models.DateTimeField()

    def __str__(self):
        return self.text[:5]