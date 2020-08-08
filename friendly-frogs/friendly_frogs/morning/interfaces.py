import abc
from dataclasses import dataclass
from datetime import datetime
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


class ConvertedUnit(abc.ABC):
    def __init__(self, metric: float = None, imperial: float = None):
        if not metric and not imperial:
            raise ValueError
        self._metric = metric
        self._imperial = imperial

    @property
    def metric(self) -> float:
        if not self._metric:
            return self.imperial_to_metric()
        return self._metric

    @property
    def imperial(self) -> float:
        if not self._imperial:
            return self.metric_to_imperial()
        return self._imperial

    @abc.abstractmethod
    def metric_to_imperial(self) -> float:
        """Implement conversion from metric to imperial"""
        raise NotImplementedError

    @abc.abstractmethod
    def imperial_to_metric(self) -> float:
        """Implement conversion from imperial to metric"""
        raise NotImplementedError


class Temperature(ConvertedUnit):
    def metric_to_imperial(self) -> float:
        return (self.metric * 9 / 5) + 32

    def imperial_to_metric(self) -> float:
        return (self.imperial - 32) * 5 / 9

    @property
    def celsius(self) -> float:
        return self.metric

    @property
    def fahrenheit(self) -> float:
        return self.imperial

    def __repr__(self):
        return f"<Temperature: celsius={self.celsius} fahrenheit={self.fahrenheit}>"


class WindSpeed(ConvertedUnit):
    def metric_to_imperial(self) -> float:
        return self.metric * 2.237

    def imperial_to_metric(self) -> float:
        return self.imperial / 2.237

    @property
    def metre_per_second(self) -> float:
        return self.metric

    @property
    def miles_per_hour(self) -> float:
        return self.imperial

    def __repr__(self):
        return f"<WindSpeed: m/s={self.metre_per_second} mph={self.miles_per_hour}>"


@dataclass
class WeatherInterface:
    temperature: Temperature
    pressure: Optional[int]  # hPa
    humidity: Optional[int]  # percent
    wind_speed: Optional[WindSpeed]
    wind_deg: Optional[int]
    time: datetime
    clouds: Optional[int]  # percent


@dataclass
class RedditInterface:
    title: str
    url: str
    content: str
    time_created_unix: int
    id: str
    subreddit: str
