from django.db import models
from django.contrib.auth.models import AbstractUser


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    pass


class Post(models.Model):
    pass


class Topic(models.Model):
    pass


class Comment(TimeStampedModel):
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    body = models.CharField(max_length=10000, default='')
    
    author = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    comment_thread = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
