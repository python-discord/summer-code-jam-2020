import pycountry
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('D', 'Other')
    )

    # TODO maybe use django-countries that does this for us, there are nice flags too
    COUNTRY_CHOICES = ((country.alpha_2, country.name) for country in pycountry.countries)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_pfp.jpg', blank=True, upload_to='profile_pics')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(blank=True, max_length=2, choices=COUNTRY_CHOICES)
    city = models.CharField(blank=True, max_length=50)
    date_of_birth = models.DateField()
    audio_track = models.FileField(null=True, blank=True, upload_to='profile_audio')
    profile_css = models.CharField(null=True, blank=True, max_length=10_000)

    def __str__(self):
        return f'{self.user.username}\'s profile'

    def __repr__(self):
        return (
            f'<Profile> {repr(self.user.username)} {repr(self.user.email)} {repr(self.image)} {repr(self.gender)} '
            f'{repr(self.country)} {repr(self.city)} {repr(self.date_of_birth)}, {repr(self.audio_track)}'
        )
