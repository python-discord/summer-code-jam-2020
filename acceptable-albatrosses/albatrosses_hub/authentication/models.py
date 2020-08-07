from django.db import models


# Create your models here.
class HubUser(models.Model):
    """A Class model that will store user information."""

    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=512)

    def __str__(self):
        # Will display user id on Django admin
        return f"({self.user_id})".zfill(3)
