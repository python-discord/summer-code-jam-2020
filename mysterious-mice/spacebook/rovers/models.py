from django.db import models


class Rover(models.Model):
    name = models.CharField(max_length=50)
    username = models.SlugField(max_length=50)
    launch_date = models.DateTimeField()
    land_date = models.DateTimeField()
    status = models.CharField(max_length=100, default=None, blank=True, null=True)
    image = models.ImageField(
        default="profile_pictures/default.jpg", upload_to="profile_pictures"
    )

    def __str__(self):
        return self.name
