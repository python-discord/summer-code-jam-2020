from django.db import models


class WikipediaArticle(models.Model):

    title = models.CharField(max_length=256)
    date = models.DateField()
    url = models.URLField()
    content = models.TextField()
