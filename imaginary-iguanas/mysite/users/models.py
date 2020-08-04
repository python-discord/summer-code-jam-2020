from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
import pycountry


class UserProfile(User):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("D", "Other")
    )
    COUNTRY_CHOICES = list((country.alpha_2, country.name) for country in pycountry.countries)

    image = models.ImageField(default="default_pfp.jpg", upload_to="profile_pics")
    gender = models.CharField(null=True, max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(null=True, max_length=2, choices=COUNTRY_CHOICES)
    city = models.CharField(null=True, max_length=50)
    date_of_birth = models.DateField(null=True)
    audio_track = models.FileField(null=True, upload_to="profile_audio")

    def __str__(self):
        return f"{self.username}'s profile"

    def __repr__(self):
        return f"<UserProfile> {repr(self.username)} {repr(self.email)} {repr(self.image)} {repr(self.gender)} {repr(self.country)} {repr(self.city)} {repr(self.date_of_birth)}"



    '''
        def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    '''

