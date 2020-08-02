from django.db import models
from django.contrib.auth.models import User

class OurUser(models.Model):
    """
    since django's user lacks some stuff that we need, this be another user model
    nickname's aren't in there yet
    """
    default_user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField()  # link to the image of the user's discord avatar
    acc_token = models.TextField()  # discord access token
    refresh_token = models.TextField()  # discord refresh token
    token_exp_date = models.DateTimeField()  # token expiration date
    discord_id = models.TextField()
