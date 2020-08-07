from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Extend default user for case when we need to add something to this."""

    pass

class BlogArticle(models.Model) :
    title           = models.CharField(max_length=100, unique=True)
    content         = models.CharField(max_length=10000)
    author          = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created    = models.DateField()

    def __str__(self) :
        return "<BlogArticle: {}>".format(self.title)
