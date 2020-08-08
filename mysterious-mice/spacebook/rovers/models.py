from django.db import models


class Rover(models.Model):
    name = models.CharField(max_length=50)
    username = models.SlugField(max_length=50, unique=True)
    about_me = models.TextField(blank=True, null=True)
    launch_date = models.DateTimeField(blank=True, null=True)
    land_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    max_speed = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Feet Per Hour",
    )
    average_speed = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Feet Per Hour",
    )
    cost = models.IntegerField(blank=True, null=True, help_text="USD")
    status = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        default="profile_pictures/default.jpg", upload_to="profile_pictures"
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return (
            f"Rover(name={self.name}, username={self.username}, launch_date={self.launch_date}, "
            f"land_date={self.land_date}, status={self.status}, image={self.image})"
        )
