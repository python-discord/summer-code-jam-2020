from django.db import models
from django.utils import timezone
from enum_field import Enum, EnumField
from user.models import ForumUser


class Thread(models.Model):
    """
    the model for a thread/conversation
    """
    title = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(ForumUser, models.DO_NOTHING)


class Message(models.Model):
    """
    the model for a message inside a thread
    """
    content = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(ForumUser, models.DO_NOTHING)  # it's either this or models.PROTECT
    date_posted = models.DateTimeField()
    date_edited = models.DateTimeField(default=date_posted)


EVENT_TYPES = Enum(
    ('create-message', 'CREATE'),
    ('view-thread', 'VIEW')
)


class UserThreadEvent(models.Model):
    """
    we log an event when the user interacts with the thread,
    whether they be viewing it or making a post
    """
    type = EnumField(EVENT_TYPES)  # idk, true would be create, and false would be view?
    thread = models.ForeignKey(Thread, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(ForumUser, models.DO_NOTHING)
