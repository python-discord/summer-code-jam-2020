from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    """ Model representing a forum thread """
    created_date = models.DateTimeField('Date created', auto_now_add=True, null=False)
    title = models.CharField(max_length=120, null=False)
    created_by = models.ForeignKey(User, on_delete=models.SET('Deleted'), to_field='username')

    def __str__(self):
        return self.title


class ThreadMessage(models.Model):
    """ Model representing a forum thread message """

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET('Deleted'), to_field='username')
    date = models.DateTimeField('Date created', auto_now_add=True)
    message = models.TextField(max_length=3000)

    def __str__(self):
        return (f'Message by {self.user} created {self.date} | '
                f'{self.message}'
                )
