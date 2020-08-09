import os
from datetime import datetime
from typing import List

import requests
import praw

from newsapi.newsapi_client import NewsApiClient

from .interfaces import NewsInterface, Temperature, WeatherInterface, WindSpeed, RedditInterface

OWM_API_KEY = os.getenv("OWM_API_KEY") or ""
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")


class News:
    '''
    External API Service for news feed
    '''
    api_key = "552022408c394577825bfd63f2d59a42"

    def __init__(self):
        self._news = NewsApiClient(api_key=self.api_key)

    def get_news(self, source: str) -> List[NewsInterface]:
        news = self._news.get_top_headlines(sources=source)
        if not news['articles']:
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


def get_current_weather(city: str, country: str) -> WeatherInterface:
    location = f"{city}, {country}"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={OWM_API_KEY}"
    r = requests.get(url)
    data = r.json()
    main = data.get("main", {})
    temperature = main.get("temp")
    pressure = main.get("pressure")
    humidity = main.get("humidity")
    wind = data.get("wind", {})
    wind_speed = wind.get("speed")
    wind_deg = wind.get("deg")
    c = data.get("clouds", {})
    clouds = c.get("all")
    timestamp = data.get("dt")
    dt = datetime.fromtimestamp(timestamp) if timestamp else datetime.now()

    return WeatherInterface(
        temperature=Temperature(metric=temperature),
        pressure=pressure,
        humidity=humidity,
        wind_speed=WindSpeed(metric=wind_speed),
        wind_deg=wind_deg,
        clouds=clouds,
        time=dt,
    )


def get_reddit_posts(subreddit: str, limit: int = 1):
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                         client_secret=REDDIT_CLIENT_SECRET,
                         user_agent=REDDIT_USER_AGENT)
    posts = []
    for post in reddit.subreddit(subreddit).top('day', limit=limit):
        if not post.selftext:
            content = post.url
        else:
            content = post.selftext
        posts.append(
            RedditInterface(
                title=post.title,
                url='https://www.reddit.com' + post.permalink,
                content=content,
                time_created_unix=post.created_utc,
                id=post.id,
                subreddit=subreddit
            )
        )
        return posts
