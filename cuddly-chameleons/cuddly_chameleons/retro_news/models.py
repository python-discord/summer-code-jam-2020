from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Extend default user for case when we need to add something to this."""

    pass


class BlogArticle(models.Model):
    """Object for blog post."""

    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<BlogArticle: {}>".format(self.title)


class ArticleComment(models.Model):
    """Model for blog article comment."""

    comment = models.CharField(max_length=10000)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(BlogArticle, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f"Comment by {self.author.username} at {self.created} for post {self.post}"
