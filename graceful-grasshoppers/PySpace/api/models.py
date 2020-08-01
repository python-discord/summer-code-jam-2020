from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Like(models.Model):
    '''A model for the likes a post got'''

    date_liked = models.DateTimeField(default=timezone.now)
    user_liked = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_liked}'s like"


class Dislike(models.Model):
    '''A model for the dislikes a post got'''

    date_disliked = models.DateTimeField(default=timezone.now)
    user_disliked = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_disliked}'s dislike"


class Post(models.Model):
    '''A model for the post a user makes'''

    title = models.CharField(max_length=150)

    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    likes = models.ManyToManyField(Like)
    dislikes = models.ManyToManyField(Dislike)

    def __str__(self):
        return f"{self.title} by {self.author}"
