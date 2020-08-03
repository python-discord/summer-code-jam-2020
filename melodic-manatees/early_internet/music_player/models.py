from django.db import models


# Create your models here.
class SongData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song_title = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return f'{self.song_title} on profile: {self.user}'

class SongFile(models.Model):
    song_songfile = models.FileField(upload_to='songs')
    song_data = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_title
