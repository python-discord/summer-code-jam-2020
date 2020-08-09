from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import namegenerator


class AnonUserManager(BaseUserManager):
    def create_user(self, id, nickname, last_seen, password):
        user = self.model(
            id=id,
            nickname=nickname,
            last_seen=last_seen)
        user.set_password(password)
        user.save()
        return user


class AnonUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=25, default=namegenerator.gen)
    last_seen = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=5, default="abcde")
    objects = AnonUserManager()
    auth_token = models.CharField(max_length=30, default="")
    auth_expiration = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'id'

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        super(AnonUser, self).save(*args, **kwargs)
