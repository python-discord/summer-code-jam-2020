import datetime

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=150)
    join_date = models.DateTimeField()
    is_author = models.BooleanField() # can they author articles?

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=30000)
    publication_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.SET(None))

    def __str__(self):
        return "".join(
            [
                "title=",
                repr(self.title),
                " author=",
                repr(self.author),
                " publication_date=",
                repr(self.publication_date.isoformat()),
            ]
        )


class Comment(models.Model):
    text = models.CharField(max_length=8000)
    publication_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.SET(None))
    parent_post = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return "".join(
            [
                "author=",
                repr(self.author),
                " publication_date=",
                repr(self.publication_date.isoformat()),
            ]
        )
