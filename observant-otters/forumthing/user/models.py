from django.db import models
from django.contrib.auth.models import AbstractUser

class ForumUser(AbstractUser):
    username = models.TextField(unique=True)
    nickname = models.TextField(default='')
    email = models.EmailField(default='none@smth.com')
    avatar = models.URLField()                        # link to the image of the user's discord avatar
    acc_token = models.TextField()                    # discord access token
    refresh_token = models.TextField()                # discord refresh token
    token_exp_date = models.DateTimeField(null=True)  # token expiration date
    discord_id = models.TextField()


    def __str__(self):  # maybe a better string repr?
        if self.nickname:
            return self.nickname
        return self.username
