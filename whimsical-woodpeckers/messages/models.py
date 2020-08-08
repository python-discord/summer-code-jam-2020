from django.db import models
from anon.models import AnonUser


class Conversation(models.Model):
    id = models.AutoField()
    participants = models.ManyToManyField(AnonUser, on_delete=models.CASCADE)
    user_one = models.ForeignKey(AnonUser, on_delete=models.CASCADE)  # User with lower id will always be user 1
    user_two = models.ForeignKey(AnonUser, on_delete=models.CASCADE)


class Messages(models.Model):
    id = models.AutoField()
    sender = models.ForeignKey(AnonUser, on_delete=models.CASCADE)
    receiver = models.ForeignKey(AnonUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    type = models.IntegerField()
    time_date = models.DateField()
    pk = models.CharField(max_length=100, default=(str(sender)+"_"+str(receiver)+"_"+str(time_date)), primary_key=True)

# class GroupMessages(models.Messages):
#    receiver = models.ForeignKey(AnonUser, on_delete=models.CASCADE)
