from newsapi import NewsApiClient
import time

def get_news_from_newsapi(source):

    newsapi = NewsApiClient(api_key='552022408c394577825bfd63f2d59a42')

    get_info = newsapi.get_top_headlines(sources=source)
    articles = get_info['articles']
    if len(articles) < 1:
        print("Sorry we don't have that feed for you")
    else:
        return articles

def get_everything_from_newsapi():

    newsapi = NewsApiClient(api_key='552022408c394577825bfd63f2d59a42')

    all_articles = newsapi.get_everything(sources='bbc-news',from_param='2020-08-06', to='2020-08-06')

    return all_articles

'''
newsapi = NewsApiClient(api_key='552022408c394577825bfd63f2d59a42')
sources = newsapi.get_sources()
NEWS_API_CHOICES = ()
for source in sources['sources']:
    temp_tup = (source['id'],source['name'])
    print(temp_tup)
    NEWS_API_CHOICES = ((NEWS_API_CHOICES,) + (temp_tup,))
    print(NEWS_API_CHOICES)
'''
     