from django.db import models


# Create your models here.

class Anonymous(models.Model):
    identifier = models.IntegerField()

    def __str__(self):
        return f'Anonymous_{self.identifier}'


class Board(models.Model):
    name = models.CharField(max_length=50)
    post_num = models.IntegerField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    poster = models.ForeignKey(Anonymous, on_delete=models.CASCADE)
    publication_date = models.DateTimeField('date published')
    text = models.TextField()

    def __str__(self):
        short_text = self.text[:100 + 1]
        short_text = short_text[:max(short_text.rfind(' '), short_text.rfind('\n'))]
        return f'{self.title}\n {short_text}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(Anonymous, on_delete=models.CASCADE)
    publication_date = models.DateTimeField('date published')
    text = models.TextField()

    def __str__(self):
        short_text = self.text[:100 + 1]
        short_text = short_text[:max(short_text.rfind(' '), short_text.rfind('\n'))]
        return short_text
