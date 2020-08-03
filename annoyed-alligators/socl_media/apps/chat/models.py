from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Chat(models.Model):
    """
    A private message from user to user
    """
    subject = models.CharField(_("Subject"), max_length=120, blank=True)
    body = models.TextField(_("Body"))
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='sender_messages',
                               verbose_name=_("Sender"),
                               on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='receiver_messages', null=True,
                                  blank=True, verbose_name=_("Recipient"),
                                  on_delete=models.CASCADE)
    parent_msg = models.ForeignKey('self', related_name='next_messages',
                                   null=True, blank=True,
                                   verbose_name=_("Parent message"),
                                   on_delete=models.CASCADE)
    sent_at = models.DateTimeField(_("sent at"), null=True, blank=True)
    read_at = models.DateTimeField(_("read at"), null=True, blank=True)
    replied_at = models.DateTimeField(_("replied at"), null=True, blank=True)
    sender_deleted_at = models.DateTimeField(_("Sender deleted at"), null=True,
                                             blank=True)
    recipient_deleted_at = models.DateTimeField(_("Recipient deleted at"),
                                                null=True, blank=True)
    ip = models.GenericIPAddressField(verbose_name=_('IP'), null=True,
                                      blank=True)
    user_agent = models.CharField(verbose_name=_('User Agent'), blank=True,
                                  max_length=255)
