from .models import GeneratedPage
import requests


# This is where the text will be scraped. Right now, this function only generates an info page with a title
def generate_page(page_name):
    page_author = generate_name()
    return GeneratedPage.objects.create(page_title=page_name, page_author=page_author, page_type='INFO',
                                        scam_type='ROMANCE')


# Returns a randomly generated name
def generate_name():
    person = requests.get('https://api.namefake.com/')
    return person.json()['name']


# This function will be used to generate text for the info style pages
def generate_information():
    pass
