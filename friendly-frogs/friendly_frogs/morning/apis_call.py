from newsapi.newsapi_client import NewsApiClient

NEWS_SOURCES = (
    ('bbc-news', 'BBC NEWS'),
)


class News:

    api_key = '552022408c394577825bfd63f2d59a42'

    def __init__(self):
        self._news = NewsApiClient(api_key=self.api_key)

    def get_news(self, source):
        news = self._news.get_top_headlines(sources=source)
        if news['articles'] == []:
            return "There is no article for you"
        else:
            return news
