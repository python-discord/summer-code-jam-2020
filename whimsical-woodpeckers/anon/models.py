from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AnonUser(models.Model):
    user = models.AutoField(primary_key=True)
    last_seen = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(AnonUser, self).save(*args, **kwargs)



