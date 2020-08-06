from django.db import models


class Guestbook(models.Model):
    page = models.TextField(default='home')
    author = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    published_date = models.DateTimeField(blank=True, null=True)
