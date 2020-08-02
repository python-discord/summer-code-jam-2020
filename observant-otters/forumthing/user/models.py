from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class ForumUser(AbstractBaseUser):
    username = models.TextField()
    nickname = models.TextField(default=username)
    avatar = models.URLField()  # link to the image of the user's discord avatar
    acc_token = models.TextField()  # discord access token
    refresh_token = models.TextField()  # discord refresh token
    token_exp_date = models.DateTimeField()  # token expiration date
    discord_id = models.TextField()

    def __str__(self):  # maybe a better string repr?
        return self.username
