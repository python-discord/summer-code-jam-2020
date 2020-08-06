from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    headline = models.TextField()
    body = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(get_user_model(), on_delete=models.SET(None))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Article({self.title=}, {self.author=}, {self.publication_date=})"


class Comment(models.Model):
    text = models.TextField()
    publication_date = models.DateTimeField()
    author = models.ForeignKey(get_user_model(), on_delete=models.SET(None))
    parent_post = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment(post={self.parent_post.id}, {self.text=}, {self.author=}, {self.publication_date=})"
