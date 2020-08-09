from django.db import models

# Create your models here.


class Result(models.Model):
    title = models.TextField()
    snippet = models.TextField()
    display_link = models.URLField()
    link = models.URLField()
