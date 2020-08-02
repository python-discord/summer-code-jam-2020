from django.db import models
from user.models import User

class Thread(models.Model):
    """
    the model for a thread/conversation
    """
    title = models.TextField()
    date_created = models.DateTimeField()
    author = models.OneToOneField(User, models.CASCADE)


class Message(models.Model):
    """
    the model for a message inside a thread
    """
    content = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.OneToOneField(User, models.DO_NOTHING)  # it's either this or models.PROTECT
    date_posted = models.DateTimeField()
    date_edited = models.DateTimeField(default=date_posted)


class UserThreadEvent(models.Model):
    """
    we log an event when the user interacts with the thread,
    whether they be viewing it or making a post
    """
    type = models.BooleanField()  # idk, true would be create, and false would be view?
    thread = models.ForeignKey(Thread, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, models.DO_NOTHING)
