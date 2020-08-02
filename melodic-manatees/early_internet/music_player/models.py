from django.db import models


# Create your models here.
class Song(models.Model):
    song_title = models.CharField(max_length=100)
    song_songfile = models.FileField(upload_to='songs')

    def __str__(self):
        return self.song_title
