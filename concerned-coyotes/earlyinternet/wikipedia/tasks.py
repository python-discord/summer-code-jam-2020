from .models import WikipediaArticle
from .utils import get_wikipedia_featured_articles


def fetch_wikipedia():
    for article in get_wikipedia_featured_articles():
        WikipediaArticle.objects.create(**article)
