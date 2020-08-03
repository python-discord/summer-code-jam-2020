from .models import GeneratedPage
import requests, wikipedia


# This is where the text will be scraped. Right now, this function only generates an info page with a title
def generate_page(page_name):
    """Gets a page object which only has a title, then populates it with scraped information"""
    page_object = GeneratedPage.objects.get(page_title=page_name)
    page_object.page_content = generate_information(page_name)
    page_object.page_author = generate_name()
    page_object.page_type = "INFO"
    page_object.scam_type = "ROMANCE"
    page_object.is_generated = True
    page_object.save()
    
    return page_object


# Returns a randomly generated name
def generate_name():
    person = requests.get('https://api.namefake.com/')
    return person.json()['name']


# This function will be used to generate text for the info style pages. For now, it downloads from wikipedia
def generate_information(page_name):
    # First searches noun in wikipedia search
    search = wikipedia.search(page_name, results=1)

    # Tries to return the contents of the first result
    try:
        result = wikipedia.summary(search[0])
    except IndexError:
        # If the search yielded no results
        result = "Under Construction"
    except wikipedia.DisambiguationError as e:
        # If the page it enters is a wikipedia "disambiguation" page
        result = wikipedia.summary(e.options[0])
    return result
