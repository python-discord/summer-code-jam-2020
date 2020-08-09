from newsapi import NewsApiClient

from .models import Article


API_KEY = "c8a36b9a701d42ca854f7c31de866ba4"


def get_news():
    """ Query and save top headlines """
    client = NewsApiClient(api_key=API_KEY)
    result = client.get_top_headlines()
    articles = result['articles']

    # save to db
    for article in articles:
        if not article['description']:
            continue
        Article.objects.create_article(article)

    print(f"Added {len(articles)} Articles")
    return articles
