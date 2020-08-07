
from django.db import models

class Conversation(models.Model):
    id = models.AutoField
    participants =
    pk =

class Messages(models.Model):
    id = models.AutoField
    sender = user.id
    reciever = user.id
    content = models.CharField(max_length=280)
    type = models.IntegerField()
    time_date = models.DateField()
    pk = (sender+"_"+reciever+"_"+time_date)

