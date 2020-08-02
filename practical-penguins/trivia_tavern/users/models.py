from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class PhoneNumber(models.Model):
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return f'{self.phone_number}'
