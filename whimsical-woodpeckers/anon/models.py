from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class AnonUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    last_seen = models.DateTimeField()
    password = models.CharField(max_length=5, default="abcde")

    USERNAME_FIELD = 'id'

    def __str__(self):
        return f'{self.id} Profile'

    def save(self, *args, **kwargs):
        super(AnonUser, self).save(*args, **kwargs)



