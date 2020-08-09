import datetime
import random

from django.test import TestCase
from django.utils.dateparse import parse_datetime

from .models import Article


class ArticleTestCase(TestCase):

    def setUp(self) -> None:
        self.article = Article.objects.create(
            source="HackerNews",
            author="Guido van Rossum",
            title="Why Python is such a nice language",
            description="...",
            content="...",
            url="http://python.org/",
            published_at=datetime.datetime(2020, 1, 1, 12, 0)
        )

    def test_representation(self):
        """ Test if Article.__str__ works correctly """
        self.assertEqual(
            str(self.article),
            "Why Python is such a nice language 2020-01-01T12:00:00"
        )

    def test_article_manager_create_article(self):
        """
        Test if Article.objects.create_article works correctly
        :return:
        """
        article = {
            'source': {'id': 'news-com-au', 'name': 'News.com.au'},
            'author': 'unknown'
            'title': 'F1 British Grand Prix live: updates, results, starting grid, Vettel reacts to Ferrari sabotage '
                     'questions',
            'description': 'The British Grand Prix has ended in incredible drama as the last lap went down to the '
                           'wire with Lewis Hamilton winning after his tyre blew on the last lap.',
            'url': 'https://www.news.com.au/sport/motorsport/formula-one/live-updates-from-the-2020-british-grand'
                   '-prix/live-coverage/ba297f46d4e91321c092db9d3d5d2e1f',
            'urlToImage': 'https://content.api.news/v3/images/bin/2554ff2213b5c8a54e9809d310e697db',
            'publishedAt': '2020-08-02T22:04:07Z',
            'content': '...'
        }
        created = Article.objects.create_article(article)
        self.assertEqual(article['source']['name'], created.source)
        self.assertEqual('unknown', created.author)
        self.assertEqual(article['title'], created.title)
        self.assertEqual(article['description'], created.description)
        self.assertEqual(article['url'], created.url)
        self.assertEqual(parse_datetime(article['publishedAt']), created.published_at)
        self.assertEqual('...', created.content)

    def test_article_manager_get_latest(self):
        """ Test Article.objects.get_latest """

        # create 10 articles
        articles = [self.article]
        for i in range(9):
            year = random.randrange(1900, 2020)
            month = random.randrange(1, 12)
            day = random.randrange(1, 28)
            hour = random.randrange(1, 24)
            article = Article.objects.create(
                source="", author="", title=str(i), description="", content="", url="http://example.org/",
                published_at=datetime.datetime(year, month, day, hour)
            )
            articles.append(article)

        # sort articles
        articles.sort(key=lambda x: x.published_at, reverse=True)

        self.assertEqual(
            articles[:4],
            list(Article.objects.get_latest(4))
        )
