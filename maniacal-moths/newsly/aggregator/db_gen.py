import requests
import json
import datetime
from .models import Article
from newspaper import Article as content_getter


class Database_Generator:
    """Gathers new articles from news sources"""

    def __init__(self):
        self.url = "https://newscatcher.p.rapidapi.com/v1/latest_headlines"
        self.topics = [
            "tech",
            "news",
            "business",
            "finance",
            "politics",
            "economics",
            "entertainment",
            "sport",
            "world",
        ]
        self.headers = {
            "x-rapidapi-host": "newscatcher.p.rapidapi.com",
            "x-rapidapi-key": "SECRET-ID-HERE",
        }

    def generate_db(self, lang="en", country="AU"):
        """Searches for articles matching the preferred language and country"""

        for topic in self.topics:
            try:
                query = {"topic": topic, "lang": lang, "country": country}
                response = requests.request(
                    "GET", self.url, headers=self.headers, params=query
                )
                data = json.loads(response.text)

                if data["status"] == "ok":
                    for article in data["articles"]:
                        auth = article.get("author", None)
                        if auth in ["None", None]:  # Sometimes the api returns the String "None"
                            auth = article.get("clean_url").lstrip("https://").lstrip("www.")
                            auth = auth.rstrip(".com").capitalize()
                            auth += " Editor"

                            cont = content_getter(article["link"])
                            cont.download().parse().nlp()
                            cont = cont.text
                            Article.objects.create(
                                title=article.get("title", "News Article"),
                                topic=article.get("topic", "General"),
                                summary=article.get("summary"),
                                published_date=article.get(
                                    "published_date", datetime.datetime.now()
                                ),
                                author=auth,
                                clean_url=article.get("clean_url", "#"),
                                link=article.get("link", "#"),
                                language=article.get("language", "en"),
                                country=article.get("country", "US"),
                                content=cont,
                            )
            except KeyError:
                print("Skipping Corrupted Article")
