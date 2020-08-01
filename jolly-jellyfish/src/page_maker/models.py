from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Webpage(models.Model):
    name = models.CharField(max_length=80)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="thumbnails/")
    template = models.IntegerField()
    # TODO add template fields


class Template(models.Model):
    name = models.CharField(max_length=80)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    style_sheet = models.FileField(null=False, blank=False, upload_to="styles/")


class Comment(models.Model):
    page = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
