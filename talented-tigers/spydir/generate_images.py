import os
import requests
from .models import PageImage


def generate_images(category: str, n: int, query:str = "clip art", image_type: str = "illustration") -> PageImage:
    """Use pixabay api to get image links based on image categories."""

    """
    Cactegories can be:
    backgrounds, fashion, nature, science, education, 
    feelings, health, people, religion, places, animals, 
    industry, computer, food, sports, transportation, 
    travel, buildings, business, music 
    """
    response = requests.get(f"https://pixabay.com/api/?q={query}&lang=en&category={category}&safesearch=true&image_type={image_type}&key={os.getenv('API_KEY')}")

    images = [PageImage(image = img['userImageURL']) for img in response.json()['hits'][:5]]
    
    return images
