from django.db import models

from djangocities.folders.models import Item
from django.conf import settings


def upload_to(instance, filename):
    return f"{settings.MEDIA_ROOT}/{instance.folder}/{filename}"


class Media(Item):
    class Meta:
        verbose_name_plural = "user_media"

    image = models.ImageField(upload_to=upload_to)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.image.name
