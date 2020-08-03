from .models import GeneratedPage
import re
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


def generate_name():
    """Returns a randomly generated name"""
    person = requests.get('https://api.namefake.com/')
    return person.json()['name']


def authorize_page(page_name):
    """Authorizes page to be generated and served on request, adding the page to the index"""
    try:
        page = GeneratedPage.objects.get(page_title=page_name)
    except GeneratedPage.DoesNotExist:
        page = GeneratedPage.objects.create(page_title=page_name)


def generate_information(page_name):
    try:
        # First tries to go to the page url
        result = wikipedia.summary(page_name, auto_suggest=False)
        print('THE PAGE EXISTS')

    except wikipedia.exceptions.DisambiguationError as e:
        # If the page it enters is a wikipedia "disambiguation" page
        result = wikipedia.summary(e.options[0], auto_suggest=False)
        print('THE PAGE EXISTS BUT IS A DISAMBIGUATION PAGE, USING THE FIRST LINK')

    except wikipedia.exceptions.PageError:
        # If the page doesnt exist, performs a search
        print('THE PAGE DOESNT EXIST, USING THE WIKIPEDIA SEARCHBAR')
        search = wikipedia.search(page_name, results=1)

        try:
            result = wikipedia.summary(search[0], auto_suggest=False)
            print('GETTING THE FIRST SEARCH RESULT')

        except IndexError:
            # If the search yielded no results
            print('NO RESULTS AFTER SEARCH')
            result = "Under Construction"

        except wikipedia.exceptions.DisambiguationError as e:
            # If the page exists it enters is a wikipedia "disambiguation" page
            result = wikipedia.summary(e.options[0], auto_suggest=False)
            print('THE FIRST RESULT IS A DISAMBIGUATION PAGE, USING THE FIRST LINK')

    return parse_result(result)


def parse_result(result):
    wordlist = result.split()
    information = ""
    for i in range(0, len(wordlist)):
        # Checks if word is capitalized and not the first word in a sentence.
        if i > 0 and wordlist[i][0].isupper() and wordlist[i - 1][len(wordlist[i - 1]) - 1] != '.':
            without_punctuation = re.sub(r'[^\w\s]', '', wordlist[i])
            information += "<a href=../../page/{0}>{1}</a>".format(without_punctuation, wordlist[i])
            authorize_page(without_punctuation)
        else:
            information += wordlist[i]
        information += ' '

    return information
