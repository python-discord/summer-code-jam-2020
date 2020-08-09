from django.db import models

from .utils import shorten_text


# Create your models here.


class Board(models.Model):
    board = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'/{self.board}/ {self.title}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    poster = models.CharField(max_length=50)
    publication_date = models.DateTimeField('date published', auto_now_add=True, blank=True)
    text = models.TextField()

    class Meta:
        ordering = ['publication_date']

    def __str__(self):
        short_text = shorten_text(self.text, 100)
        return f'{self.title} - {short_text}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=50)
    publication_date = models.DateTimeField('date published', auto_now_add=True, blank=True)
    text = models.TextField()

    class Meta:
        ordering = ['publication_date']

    def __str__(self):
        short_text = shorten_text(self.text, 100)
        return short_text
