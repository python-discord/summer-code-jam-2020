from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Post(models.Model):
    pass


class Topic(models.Model):
    pass


class Comment(models.Model):
    pass
