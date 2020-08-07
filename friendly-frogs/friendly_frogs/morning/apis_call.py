from newsapi.newsapi_client import NewsApiClient


class News:
    '''
    External API Service for news feed
    '''

    api_key = '552022408c394577825bfd63f2d59a42'

    def __init__(self):
        self._news = NewsApiClient(api_key=self.api_key)

    def get_news(self, source):
        news = self._news.get_top_headlines(sources=source)
        if not news['articles']:
            return "There is no article for you"
        else:
            return news
