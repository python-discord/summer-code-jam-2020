from django.db import models

from djangocities.user.models import CustomUser as User


def upload_to(instance, filename):
    username = instance.owner.username
    return f"/cdn/user/{username}/{filename}"


class Media(models.Model):
    class Meta:
        verbose_name_plural = "user_media"

    image = models.ImageField(upload_to=upload_to)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name
