import abc
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


class ConvertedUnit(abc.ABC):
    def __init__(self, metric: float = None, imperial: float = None):
        if not metric and not imperial:
            raise Exception
        elif metric:
            self.metric = metric
            if not imperial:
                self.imperial = self.metric_to_imperial(self.metric)
        elif imperial:
            self.imperial = imperial
            if not metric:
                self.metric = self.imperial_to_metric(self.imperial)

    @staticmethod
    @abc.abstractmethod
    def metric_to_imperial(metric: float) -> float:
        """Implement conversion from metric to imperial"""
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def imperial_to_metric(imperial: float) -> float:
        """Implement conversion from imperial to metric"""
        raise NotImplementedError


class Temperature(ConvertedUnit):
    @staticmethod
    def metric_to_imperial(metric: float) -> float:
        return (metric * 9 / 5) + 32

    @staticmethod
    def imperial_to_metric(imperial: float) -> float:
        return (imperial - 32) * 5 / 9


@dataclass
class WeatherInterface:
    temperature: Temperature
