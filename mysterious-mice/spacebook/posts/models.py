from django.db import models
from rovers.models import Rover


class ImagePost(models.Model):
    image = models.ImageField(upload_to="images")
    image_id = models.IntegerField(default=0)
    description = models.TextField()
    date = models.DateTimeField()
    sol = models.IntegerField(default=0)
    rover = models.ForeignKey(Rover, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
