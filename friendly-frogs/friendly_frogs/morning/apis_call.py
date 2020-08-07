from typing import List

from newsapi.newsapi_client import NewsApiClient

from .interfaces import NewsInterface

NEWS_SOURCES = (("bbc-news", "BBC NEWS"),)


class News:
    api_key = "552022408c394577825bfd63f2d59a42"

    def __init__(self):
        self._news = NewsApiClient(api_key=self.api_key)

    def get_news(self, source: str) -> List[NewsInterface]:
        news = self._news.get_top_headlines(sources=source)
        if not news["articles"]:
            return []
        else:
            articles = list()
            for article in news["articles"]:
                source = article.get("source", {}).get("name")
                articles.append(
                    NewsInterface(
                        title=article.get("title"),
                        description=article.get("description"),
                        url=article.get("url"),
                        source=source,
                        author=article.get("author"),
                        thumbnail_url=article.get("urlToImage"),
                    )
                )
            return articles
