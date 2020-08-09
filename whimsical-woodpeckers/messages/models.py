from django.db import models
from anon.models import AnonUser


class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    # participants = models.ManyToManyField(AnonUser, on_delete=models.CASCADE)
    # User with lower id will always be user 1
    user_one = models.ForeignKey(AnonUser, related_name="%(app_label)s_%(class)s_one", on_delete=models.CASCADE)
    user_two = models.ForeignKey(AnonUser, related_name="%(app_label)s_%(class)s_two", on_delete=models.CASCADE)


class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(AnonUser, related_name="%(app_label)s_%(class)s_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(AnonUser, related_name="%(app_label)s_%(class)s_receiver", on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    type = models.IntegerField()
    time_date = models.DateField()
    # pk = models.CharField(max_length=100, default=(str(sender)+"_"+str(receiver)+"_"+str(time_date)))


class UserChannels(models.Model):
    name = models.CharField(max_length=60)
    user = models.ForeignKey(AnonUser, on_delete=models.CASCADE)

# class GroupMessages(models.Messages):
#    receiver = models.ForeignKey(AnonUser, on_delete=models.CASCADE)
