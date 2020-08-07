import os
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from users.models import UserProfile


# def rename(path, background_title):
#     def wrapper(instance, filename):
#         filename = f'{instance.background_title}_{uuid4()}'
#         return os.path.join(path, filename)
#     return wrapper


class BackgroundFile(models.Model):
    background_title = models.CharField(
        max_length=100,
        default=None
        )
    background_file = models.FileField(
        upload_to=('backgrounds/'),
        default=None
        )
    background_owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
        )
    background_thumbnail = models.ImageField(
        upload_to=('backgrounds/'),
        default=None
    )

    def __str__(self):
        return self.background_title


@receiver(post_delete, sender=BackgroundFile)
def delete_file(sender, instance, **kwargs):
    if instance.background_file:
        if os.path.isfile(instance.background_file.path):
            os.remove(instance.background_thumbnail.path)
            os.remove(instance.background_file.path)
