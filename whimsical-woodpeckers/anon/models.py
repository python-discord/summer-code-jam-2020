from django.db import models

# Create your models here.

class AnonUser(models.Model):
    id = models.AutoField(primary_key=True)
    last_seen = models.DateTimeField()



