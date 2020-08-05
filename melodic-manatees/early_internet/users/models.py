from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    background_image = models.ImageField(upload_to="backgrounds", default='backgrounds/sunrise.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
