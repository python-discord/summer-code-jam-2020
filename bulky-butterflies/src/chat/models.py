from django.contrib.auth import get_user_model
from django.db import models


class Message(models.Model):
    """
    This class represents a chat message. It has a owner (user), timestamp and
    the message body.
    """
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='user',
        related_name='from_user', db_index=True
    )
    recipient = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='recipient',
        related_name='to_user',
        db_index=True
    )
    timestamp = models.DateTimeField(
        'timestamp', auto_now_add=True, editable=False, db_index=True
    )
    body = models.TextField('body')

    def __str__(self):
        return str(self.pk)

    class Meta:
        ordering = ('-timestamp',)
