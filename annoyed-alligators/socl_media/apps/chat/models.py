from django.db import models
from django.utils import timezone
from django.conf import settings


class Message(models.Model):
    """A message from user to user with fields:

    body: contains the actual message
    sender: user sending the message
    recipient: user receiving the message
    sent_at: time at which the message was sent
    """

    body = models.TextField(("Body"))
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='sender_messages',
                               verbose_name=("Sender"),
                               on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='receiver_messages',
                                  verbose_name=("Recipient"),
                                  on_delete=models.CASCADE)
    sent_at = models.DateTimeField(("sent at"), default=timezone.now)
