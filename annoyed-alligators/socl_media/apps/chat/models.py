from django.db import models
from django.conf import settings

# Create your models here.


class Message(models.Model):
    """
    A private message from user to user
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
    sent_at = models.DateTimeField(("sent at"), null=True, blank=True)
    replied_at = models.DateTimeField(("replied at"), null=True, blank=True)
    ip = models.GenericIPAddressField(verbose_name=('IP'), null=True,
                                      blank=True)
    user_agent = models.CharField(verbose_name=('User Agent'), blank=True,
                                  max_length=255)
