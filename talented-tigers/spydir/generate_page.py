from .models import GeneratedPage
import requests, wikipedia, nltk, re
from faker import Faker



# TODO: Make the requests asynchronous
def generate_page(page_name, page_type=None):
    """Gets a page object which only has a title, then populates it with scraped information"""
    page_object = GeneratedPage.objects.get(page_title=page_name)

    possible_page_types = [page_type[0] for page_type in GeneratedPage.page_type_choices]
    # Chooses a random page type from a list of all page types. weights are in this order:
    # BLOG, INFO, BIZ, FOOD, SCAM
    page_object.page_type = random.choices(possible_page_types, [0.3, 0.5, 0.1, 0.05, 0.05])[0] if page_type is None else page_type

    # Define the different fields needed for different page types here
    if page_object.page_type == 'BLOG':
        page_object.page_author = generate_page_author()
        page_object.blogger_age = random.randrange(8, 95)
        page_object.blogger_location = generate_blogger_location()

    elif page_object.page_type == 'INFO':
        page_object.page_content = generate_information(page_name)
        page_object.page_author = generate_page_author()

    elif page_object.page_type == 'BIZ':
        pass

    elif page_object.page_type == 'FOOD':
        pass

    elif page_object.page_type == 'SCAM':
        possible_scam_types = [scam_type[0] for scam_type in GeneratedPage.scam_type_choices]
        page_object.scam_type = random.choice(possible_scam_types)

    page_object.is_generated = True
    page_object.save()

    return page_object


def generate_page_author():
    """Returns a randomly generated name"""
    fake = Faker()
    return fake.name()


def generate_blogger_location():
    """Returns a randomly generated city name"""
    fake = Faker()
    return fake.city()


def authorize_page(page_name):
    """Authorizes page to be generated and served on request, adding the page to the index"""
    try:
        page = GeneratedPage.objects.get(page_title=page_name)
    except GeneratedPage.DoesNotExist:
        page = GeneratedPage.objects.create(page_title=page_name, css_seed=random.randint(1000, 9999))


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
    for word in wordlist:
        word_token = nltk.word_tokenize(str(word))
        if nltk.pos_tag(word_token)[0][1] == "NN" or nltk.pos_tag(word_token)[0][1] == "NNP":
            without_punctuation = re.sub(r'[^\w\s]', '', word)
            information += "<a href=../../page/{0}>{1}</a>".format(without_punctuation, word)
            authorize_page(without_punctuation)
        else:
            information += word
        information += ' '

    return information
