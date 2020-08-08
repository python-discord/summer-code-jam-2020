from typing import Dict, Union

from django.db import models
from django.utils.dateparse import parse_datetime


class ArticleManager(models.Manager):

    def create_article(self, raw_article: Dict[str, Union[str, Dict[str, str]]]):
        """
        Create a new article in the database from the json data given
        by NewsApiClient.get_top_headlines['articles']

        >>> Article.objects.create_article({...})

        :param raw_article: Dictionary containing information about the article
        :return: New instance of Article
        """

        # convert timezone aware iso date string to datetime.datetime
        published_at = parse_datetime(raw_article['publishedAt'])

        if raw_article['author'] is None:
            raw_article['author'] = 'unknown'

        if raw_article['content'] is None:
            raw_article['content'] = '...'

        article = self.create(
            source=raw_article['source']['name'],
            author=raw_article['author'],
            title=raw_article['title'],
            description=raw_article['description'],
            content=raw_article['content'],
            url=raw_article['url'],
            published_at=published_at
        )
        return article

    def get_latest(self, n_items):
        """
        Return the latest n articles

        :param n_items: How many articles to return
        :return: List of n newest articles
        """
        return super().get_queryset().order_by("-published_at")[:n_items]


class Article(models.Model):

    objects = ArticleManager()
    # now we can do
    # >>> Article.objects.create_article({...})

    source = models.CharField(max_length=256)
    author = models.CharField(default="unknown", max_length=256)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    content = models.CharField(max_length=200)
    url = models.URLField()
    # in utc
    published_at = models.DateTimeField()

    def __str__(self):
        return f"{self.title} {self.published_at.isoformat()}"
