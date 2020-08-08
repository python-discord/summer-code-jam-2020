from dataclasses import dataclass
from typing import Optional


@dataclass
class NewsInterface:
    title: str
    description: str
    url: str
    source: Optional[str]
    author: Optional[str]
    thumbnail_url: Optional[str]

    def __repr__(self):
        return f'<NewsInterface::Title: "{self.title}"; Description: "{self.description}">'


class Temperature:
    def __init__(self, celsius: float = None, fahrenheit: float = None):
        if not celsius and not fahrenheit:
            raise Exception
        elif celsius:
            self.celsius = celsius
        elif fahrenheit:
            self.fahrenheit = fahrenheit


@dataclass
class WeatherInterface:
    temperature: Temperature
