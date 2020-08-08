from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Extend default user for case when we need to add something to this."""

    pass


class BlogArticle(models.Model):
    """Object for blog post."""

    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<BlogArticle: {}>".format(self.title)
