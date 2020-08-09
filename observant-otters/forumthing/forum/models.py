from django.db import models
from django.utils import timezone
from django.urls import reverse
from user.models import ForumUser

TOPICS = ['General', 'Coding', 'Jokes']


class Thread(models.Model):
    """
    the model for a thread/conversation
    """
    topic = models.CharField(max_length=50, default='General')
    title = models.CharField(max_length=200)
    content = models.TextField(default="")
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(ForumUser, models.DO_NOTHING)

    def __str__(self):
        return f'Thread with title {self.title} created on {self.date_created}'

    def get_absolute_url(self):
        return reverse('threads-single', kwargs={'pk': self.pk})


class Message(models.Model):
    """
    the model for a message inside a thread
    """
    content = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(ForumUser, models.DO_NOTHING)
    date_posted = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Message posted on {self.date_posted} with content {self.content}'

    def get_absolute_url(self):
        return reverse('threads-single', kwargs={'pk': self.thread.pk})
