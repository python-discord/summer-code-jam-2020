from django.test import TestCase
from morning.apis_call import News


class TestApiNews(TestCase):
    '''
    Testing an external API Service
    '''

    def test_api_news_connection(self):
        news = News()
        news = news.get_news('aaaaaaa')
        self.assertEqual()
        # Should be implemented mocking system. Test is not finished
