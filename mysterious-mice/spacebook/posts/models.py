from django.db import models
from rovers.models import Rover


class ImagePost(models.Model):
    image = models.ImageField(upload_to="images")
    image_id = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        help_text="NASA's image ID associated with the photo.",
    )
    description = models.TextField(default=None, blank=True, null=True)
    date = models.DateTimeField()
    sol = models.IntegerField(
        default=0, help_text="Number of Mars-days since the rover's landing."
    )
    rover = models.ForeignKey(Rover, on_delete=models.CASCADE)

    def __str__(self):
        if self.description is None or self.description == "":
            # if no description provided, return the rover's username
            return f"{self.rover.username}'s Image"
        else:
            return self.description
