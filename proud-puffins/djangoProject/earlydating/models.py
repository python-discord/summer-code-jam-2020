from django.db import models
from django.contrib.auth.models import User
from . import puffin_functions as pf

# Create your models here.
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(null=True)
    img = models.ImageField(upload_to='static/user_pixel', null=True, blank=True)
    greeting = models.CharField(max_length=200, null=True, default="Greeting")
    activity = models.CharField(max_length=200, null=True, default="Activity")
    adjective1 = models.CharField(max_length=200, null=True, default="Adjective")
    verb0 = models.CharField(max_length=200, null=True, default="Verb")
    direction = models.CharField(max_length=200, null=True, default="Direction")
    pastverb = models.CharField(max_length=200, null=True, default="Pastverb")
    noun1 = models.CharField(max_length=200, null=True, default="Noun")
    adjective2 = models.CharField(max_length=200, null=True, default="Adjective")
    verb1 = models.CharField(max_length=200, null=True, default="Verb")
    noun2 = models.CharField(max_length=200, null=True, default="Noun")
    verb2 = models.CharField(max_length=200, null=True, default="Verb")
    noun3 = models.CharField(max_length=200, null=True, default="Noun")
    noun4 = models.CharField(max_length=200, null=True, default="Noun")
    verb3 = models.CharField(max_length=200, null=True, default="Verb")
    noun5 = models.CharField(max_length=200, null=True, default="Pluralnoun")
    noun6 = models.CharField(max_length=200, null=True, default="Pluralnoun")
    exclamation = models.CharField(max_length=200, null=True, default="Exclamation")
    verb4 = models.CharField(max_length=200, null=True, default="Verb")
    verb5 = models.CharField(max_length=200, null=True, default="Verb")
    SignOff = models.CharField(max_length=200, null=True, default="Name")

    def __str__(self):
        return str(self.user)


    def save(self, *args, **kwargs):
        self.img = pf.imageTrans(self.img)
        super().save(*args, **kwargs)
