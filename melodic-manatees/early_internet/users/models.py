from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    background_image = models.FileField(
        upload_to=('backgrounds/'),
        default='defaults/sunrise.jpg'
    )

    def __str__(self):
        return f'{self.user.username} Profile'


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Weather preference for the weather section, choices, to avoid bad inputs.
    COLD = 'COLD'
    NORMAL = 'NORM'
    WARM = 'WARM'
    WEATHER_PREFERENCE_CHOICES = [
        (COLD, 'I tend to be cold!'),
        (NORMAL, 'Normal'),
        (WARM, 'Warm, I am on fire!'),
    ]
    weather_preference = models.CharField(
        max_length=4,
        choices=WEATHER_PREFERENCE_CHOICES,
        default=NORMAL,
    )

    # Need to configure a timezone field to allow UTC+/- that aren't server dependent.
    # time_zone

    # If a user wants to change their display name instead of their User object's name registered.
    name_preference = models.CharField(max_length=20)

    # Display preferences for apps to be displayed?  Defaults all to be on.
    display_weather = models.BooleanField(default=True)
    display_news = models.BooleanField(default=True)
    display_music = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} Preferences'
