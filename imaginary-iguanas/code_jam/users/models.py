from datetime import date

import pycountry
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator

from .validators import valid_age_validator


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('D', 'Other')
    )

    # TODO maybe use django-countries that does this for us, there are nice flags too
    COUNTRY_CHOICES = ((country.alpha_2, country.name) for country in pycountry.countries)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    image = models.ImageField(default='default_pfp.png', blank=True, upload_to='profile_pics')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(blank=True, max_length=2, choices=COUNTRY_CHOICES)
    place = models.CharField(blank=True, max_length=50)
    date_of_birth = models.DateField(validators=[valid_age_validator])
    audio_track = models.FileField(null=True, blank=True, upload_to='profile_audio')
    custom_css = models.TextField(blank=True, max_length=10_000, validators=[MaxLengthValidator(10_000)])

    def __str__(self):
        return f'{self.user.username}\'s profile'

    def __repr__(self):
        return (
            f'<Profile> {repr(self.user.username)} {repr(self.user.email)} {repr(self.image)} {repr(self.gender)} '
            f'{repr(self.country)} {repr(self.place)} {repr(self.date_of_birth)}, {repr(self.audio_track)}'
        )

    def age(self):
        return (date.today() - self.date_of_birth).days // 365
