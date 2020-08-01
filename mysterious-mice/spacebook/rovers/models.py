from django.db import models


class Rover(models.Model):
    name = models.CharField(max_length=50)
    username = models.SlugField(max_length=50)
    launch_date = models.DateTimeField()
    land_date = models.DateTimeField()

    def __str__(self):
        return self.name
