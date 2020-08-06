from django.db import models
from django.contrib.auth.models import User
from . import puffin_functions as pf

# Create your models here.
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

Gender_Choices = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
Pref_Choices = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Both', 'Both'))


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(null=True)
    img = models.ImageField(upload_to='static/user_pixel', validators=[pf.validate_file_size],
                            null=True, default="/static/images/Proud_Puffin_default_user.jpg")
    sex = models.CharField(max_length=10, null=True, blank=True, choices=Gender_Choices)
    preference = models.CharField(max_length=10, null=True, blank=True, choices=Pref_Choices)
    lower_age = models.PositiveSmallIntegerField(null=True)
    upper_age = models.PositiveSmallIntegerField(null=True)
    bio = models.TextField(default="")
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


class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, related_name='given_vote', on_delete=models.CASCADE)
    vote = models.BooleanField(default='')

    class Meta:
        unique_together = (('user', 'voter'))
