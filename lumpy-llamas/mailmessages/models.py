from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PrivateMessage(models.Model):
    """Model representing a private message from one user to another"""
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user', to_field='username')
    message = message = models.TextField(max_length=3000)
    subject = models.CharField(max_length=120, null=False)
    created_date = models.DateTimeField('Date created', auto_now_add=True, null=False)

    def __str__(self):
        return (f'Sender: {self.from_user}'
                f'Recipient: {self.to_user}'
                f'Sent: {self.created_date}'
                f'Subject: {self.subject}'
                f'Message: {self.message}'
                )
