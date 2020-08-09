import os
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from users.models import UserProfile


class BackgroundFile(models.Model):
    '''Model field for background image instances'''
    background_title = models.CharField(
        max_length=100,
        default=None
    )
    background_file = models.FileField(
        upload_to=('backgrounds/'),
        default='defaults/sunrise.jpg'
    )
    background_owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )
    # created using the image resizer utility from background_utility
    background_thumbnail = models.ImageField(
        upload_to=('backgrounds/'),
        default=None
    )

    def __str__(self):
        return self.background_title

# post_save signal to delete the background image
# and its thumbnail on pressing the delete button
@receiver(post_delete, sender=BackgroundFile)
def delete_file(sender, instance, **kwargs):
    if instance.background_thumbnail:
        os.remove(instance.background_thumbnail.path)
    if instance.background_file:
        if os.path.isfile(instance.background_file.path):
            os.remove(instance.background_file.path)
