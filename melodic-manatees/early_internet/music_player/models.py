import os
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from users.models import UserProfile


class MusicFile(models.Model):
    music_musicfile = models.FileField(upload_to='songs', default=None)
    music_title = models.CharField(max_length=100, default=None)
    music_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.music_title

def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)

@receiver(post_delete, sender=MusicFile)
def submission_delete(sender, instance, **kwargs):
    if instance.music_musicfile:
        _delete_file(instance.music_musicfile.url)
