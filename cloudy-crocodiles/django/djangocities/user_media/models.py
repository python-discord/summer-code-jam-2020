from django.db import models

from djangocities.folders.models import FolderItem


def upload_to(instance, filename):
    username = instance.owner.username
    return f"/cdn/user/{username}/{filename}"


class Media(FolderItem):
    class Meta:
        verbose_name_plural = "user_media"

    image = models.ImageField(upload_to=upload_to)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.image.name
