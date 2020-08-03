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
    greeting = models.CharField(max_length=200,null=True, default="Greeting")
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
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.img = pf.imageTrans(self.img)
        super().save(*args, **kwargs)
