import os
from datetime import datetime
from typing import List

import requests

from newsapi.newsapi_client import NewsApiClient

from .interfaces import NewsInterface, Temperature, WeatherInterface, WindSpeed

NEWS_SOURCES = (("bbc-news", "BBC NEWS"),)
OWM_API_KEY = os.getenv("OWM_API_KEY") or ""


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


def get_current_weather(location: str) -> WeatherInterface:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&unit=metric&appid={OWM_API_KEY}"
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
