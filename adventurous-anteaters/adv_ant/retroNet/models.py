from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tweet(models.Model):
    content = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, null=True, max_length=100)

    class Meta:
        ordering = ['-content']

    def __str__(self):
        return self.content
