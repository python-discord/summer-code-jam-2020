import random
import re
import wikipedia
import nltk
import threading
from faker import Faker
from .generate_images import generate_images
import gpt_2_simple as gpt2
from .models import GeneratedPage, BlogPost


def generate_page(page_name, page_type=None):
    """Gets a page object which only has a title, then populates it with scraped information"""
    page_object = GeneratedPage.objects.get(page_title=page_name)

    possible_page_types = [page_type[0] for page_type in GeneratedPage.page_type_choices]
    # Chooses a random page type from a list of all page types. weights are in this order:
    # BLOG, INFO, BIZ
    page_object.page_type = (
        random.choices(possible_page_types, [0.25, 0.5, 0.25])[0] if page_type is None else page_type
    )

    # Define the different fields needed for different page types here
    if page_object.page_type == "BLOG":
        page_object.page_author = generate_page_author()
        page_object.blogger_age = random.randrange(8, 95)
        page_object.blogger_location = generate_blogger_location()

        # Generates x amount of blog posts
        no_posts = (int(str(page_object.css_seed)[0]) // 2) + 1
        titles = []
        for x in range(no_posts):
            title = generate_blog_post_title(page_name)
            titles.append(title)
            blog_post = BlogPost.objects.create(title=title, content="Loading...")
            blog_post.save()
            page_object.blog_posts.add(blog_post)

        post_thread = threading.Thread(target=generate_gpt2, args=(page_object.blog_posts,))
        post_thread.start()

    elif page_object.page_type == "INFO":
        wikipedia_page = generate_information(page_name)
        page_object.page_content = wikipedia_page[0]
        page_object.page_source_url = wikipedia_page[1]
        page_object.page_author = generate_page_author()

        page_images = generate_images(False, 1, page_name)
        for page_image in page_images:
            page_image.save()
            page_object.page_images.add(page_image)

    elif page_object.page_type == "BIZ":
        faker = Faker()
        page_object.business_phone_num = faker.phone_number()
        page_object.business_email = faker.email()

        page_images = generate_images(False, 1, page_name)
        for page_image in page_images:
            page_image.save()
            page_object.page_images.add(page_image)

        page_object.business_about = "Loading. . ."
        page_object.business_mission = "Loading. . ."

        info_thread = threading.Thread(target=generate_business_statements, args=(page_name, page_object,))
        info_thread.start()

    page_object.is_generated = True
    page_object.save()

    return page_object


def generate_blog_post_title(page_name):
    titles = [
        f"I can't get over how much I love {page_name}",
        f"Let me tell you all about {page_name}",
        f"My favorite thing about {page_name}",
        f"Is it bad that I'm attracted to {page_name}?",
        f"{page_name} is the best thing ever",
        f"Is it possible to like {page_name} too much?",
    ]
    return random.choice(titles)


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
        GeneratedPage.objects.get(page_title=page_name)
    except GeneratedPage.DoesNotExist:
        GeneratedPage.objects.create(page_title=page_name, css_seed=random.randint(1000, 9999))


def generate_information(page_name):
    try:
        # First tries to go to the page url
        page = wikipedia.page(page_name, auto_suggest=False)
        print("THE PAGE EXISTS")

    except wikipedia.exceptions.DisambiguationError as e:
        # If the page it enters is a wikipedia "disambiguation" page
        page = wikipedia.page(e.options[0], auto_suggest=False)
        print("THE PAGE EXISTS BUT IS A DISAMBIGUATION PAGE, USING THE FIRST LINK")

    except wikipedia.exceptions.PageError:
        # If the page doesnt exist, performs a search
        print("THE PAGE DOESNT EXIST, USING THE WIKIPEDIA SEARCHBAR")
        search = wikipedia.search(page_name, results=1)

        try:
            page = wikipedia.page(search[0], auto_suggest=False)
            print("GETTING THE FIRST SEARCH RESULT")

        except IndexError:
            # If the search yielded no results
            print("NO RESULTS AFTER SEARCH")
            result = "Under Construction"
            return [result, ""]

        except wikipedia.exceptions.DisambiguationError as e:
            # If the page exists it enters is a wikipedia "disambiguation" page
            page = wikipedia.page(e.options[0], auto_suggest=False)
            print("THE FIRST RESULT IS A DISAMBIGUATION PAGE, USING THE FIRST LINK")

    page_summary = page.summary
    page_url = page.url
    return [parse_result(page_summary), page_url]


def parse_result(result):
    wordlist = result.split()
    information = ""
    for word in wordlist:
        word_token = nltk.word_tokenize(str(word))
        if nltk.pos_tag(word_token)[0][1] == "NN" or nltk.pos_tag(word_token)[0][1] == "NNP":
            without_punctuation = re.sub(r"[^\w\s]", "", word)
            information += "<a href=../../page/{0}>{1}</a>".format(without_punctuation, word)
            authorize_page(without_punctuation)
        else:
            information += word
        information += " "

    return information


# TODO: Make the page update without refreshing
def generate_gpt2(posts):
    # Currently, the model is loaded everytime this function is called, which may be slow. Putting it outside doesnt
    # work
    model_name = "124M"
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, model_name=model_name)

    for post in posts.all():
        post.content = "Generating..."
        post.save()
        output = gpt2.generate(
            sess, model_name=model_name, model_dir="models", return_as_list=True, prefix=post.title, length=100
        )[0]

        post.content = parse_result(splice_sentence(output))
        post.save()


def generate_business_statements(page_name, page_object):
    # Currently, the model is loaded everytime this function is called, which may be slow. Putting it outside doesnt
    # work
    model_name = "124M"
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, model_name=model_name)

    about = gpt2.generate(
        sess, model_name=model_name, model_dir="models", return_as_list=True, prefix=f"{page_name} Co. is", length=100
    )[0]
    page_object.business_about = parse_result(splice_sentence(about))
    page_object.save()

    mission = gpt2.generate(
        sess, model_name=model_name, model_dir="models", return_as_list=True, prefix="Our Mission", length=100
    )[0]
    page_object.business_mission = parse_result(splice_sentence(mission))
    page_object.save()


def splice_sentence(word):
    cutoff = max([word.rfind("."), word.rfind("?"), word.rfind("!")])
    return word[: cutoff + 1]
