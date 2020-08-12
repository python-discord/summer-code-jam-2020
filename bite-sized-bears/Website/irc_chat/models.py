from django.db import models

from syndication_app.models import User


class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    community = models.TextField(default='old_messages')

    def __str__(self):
        return self.author.name + ':' + self.content

    def last_15_messages(self, community):
        return Message.objects.filter(community=community).order_by('-timestamp').all()[:15:-1]


class UserProfile(models.Model):
    community = models.TextField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.community + ", count: " + str(self.count)
