from django.db import models

from djangocities.user.models import CustomUser as User

class Media(models.Model):
    class Meta:
        verbose_name_plural = "user_media"

    image = models.ImageField(upload_to='uploads')
    description = models.TextField(blank=True)
    directory = models.CharField(max_length=256)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name
