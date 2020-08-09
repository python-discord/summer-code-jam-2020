import os
import requests
from .models import PageImage


def generate_images(category, n: int, query: str = "clipart") -> list:
    """Use pixabay api to get image links based on image categories."""

    """
    Categories can be:
    backgrounds, fashion, nature, science, education,
    feelings, health, people, religion, places, animals,
    industry, computer, food, sports, transportation,
    travel, buildings, business, music
    """
    rq = (
        f"https://pixabay.com/api/?q={query}&lang=en{'&category=' + category if category else ''}&safesearch=true&key="
        f"{os.getenv('API_KEY')}"
    )
    response = requests.get(rq)
    return [PageImage(image=img["webformatURL"]) for img in response.json()["hits"][:n]]
