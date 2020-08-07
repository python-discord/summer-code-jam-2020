import os
import requests
from .models import PageImage


def generate_images(category, n: int, query: str = "clip art", image_type: str = "illustration") -> list:
    """Use pixabay api to get image links based on image categories."""

    """
    Categories can be:
    backgrounds, fashion, nature, science, education,
    feelings, health, people, religion, places, animals,
    industry, computer, food, sports, transportation,
    travel, buildings, business, music
    """

    response = requests.get(
        "https://pixabay.com/api/?"
        f"q={query}"
        "&lang=en"
        f"{'&category=' + category if category else ''}"
        "&safesearch=true"
        f"&image_type={image_type}"
        f"&key={os.getenv('API_KEY')}"
    )

    return [PageImage(image=img["userImageURL"]) for img in response.json()["hits"][:5]]
