from django.db import models
from . import puffin_functions as pf

# Create your models here.


class Profile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
        )

    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER)
    img = models.ImageField(upload_to='static/user_pixel', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.img = pf.imageTrans(self.img)
        super().save(*args, **kwargs)
