from django.test import TestCase
from morning.apis_call import News

class TestApiNews(TestCase):

    def test_api_news_connection(self):
        news = News()
        news = news.get_news('aaaaaaa')
        
        self.assertEqual()

