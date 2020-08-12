from django.db import models
from django.contrib.auth.models import User
from . import puffin_functions as pf


# Create your models here.
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

Gender_Choices = (('Male', 'Male'), ('Female', 'Female'))
Pref_Choices = (('straight', 'straight'), ('gay', 'gay'), ('bisexual', 'bisexual'))


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(null=True)
    img = models.ImageField(upload_to='user_pixel', validators=[pf.validate_file_size],
                            null=True, default="images/Proud_Puffin_default_user.jpg")
    sex = models.CharField(max_length=10, null=True, blank=True, choices=Gender_Choices)
    preference = models.CharField(max_length=10, null=True, blank=True, choices=Pref_Choices)
    bio = models.TextField(default="")
    upper_age = models.PositiveSmallIntegerField(null=True)
    lower_age = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if 'user_pixel' in self.img.path:
            pass
        else:
            self.img = pf.imageTrans(self.img)

        super(Profile, self).save(*args, **kwargs)


class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, related_name='given_vote', on_delete=models.CASCADE)
    vote = models.BooleanField(default=False)

    class Meta:
        unique_together = (('user', 'voter'))

    def __str__(self):
        return f"{self.voter} {'likes' if self.vote else 'dislikes'} {self.user}"
