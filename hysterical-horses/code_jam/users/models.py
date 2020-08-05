from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"{self.user.username} Profile"

    @property
    def score(self):
        return len(self.user.all_likes.all()) + len(self.user.posts.all())
