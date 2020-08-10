from django.db import models
import datetime
# Create your models here.


class Comment(models.Model):
    content = models.CharField(max_length=3000,help_text="",)
    publish_date = models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return self.content


class Video(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    publisher = models.CharField(max_length=30)
    view_count = models.IntegerField(default=0)
    now_playing = models.BooleanField(default=False)

    def __str__(self):
        return self.name

