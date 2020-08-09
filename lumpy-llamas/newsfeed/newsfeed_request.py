import requests
from requests.exceptions import HTTPError
from multiprocessing.dummy import Pool
THREAD_POOL = Pool(8)
HACKERNEWS_URL = 'https://hacker-news.firebaseio.com/v0'


# Function to get the new stories from the API, the output of this is a list with numbers
# each number represents a new story, there are maximum 500 newstories
def get_new_stories() -> list:
    # newstories.json? refers to the new stories in the API
    response = requests.get(f'{HACKERNEWS_URL}/newstories.json?')
    return response.json()


# Function to get the best stories from the API, the output of this is a list with numbers
# each number represents a top story, there are maximum 500 best stories
def get_best_stories() -> list:
    # beststories.json? refers to the best stories in the API
    response = requests.get(f'{HACKERNEWS_URL}/beststories.json?')
    return response.json()


def get_story(story_id):
    api_response = requests.get(f'{HACKERNEWS_URL}/item/{story_id}.json').json()
    print(api_response)
    # if api_response.get("url") is not None:
    filtered_dict = {
        "url": api_response.get("url"),
        "title": api_response.get("title")
    }
    return filtered_dict


# Function to retrieve the articles, this can either be the new stories or the best stories
# the output of this function depends on the input of the arguments
def retrieve_articles(stories_list, number_articles):
    # define an empty list and set index to 0
    # avoid out of range value for number_articles (our max is 5)
    if number_articles > 5:
        number_articles = 5

    # iterating trough the required number of articles
    # if an article has no url, the next available article with url is taken
    # the articles are appended one by one to a list
    stories_to_get = stories_list[:number_articles]
    try:
        articles = THREAD_POOL.map(get_story, stories_to_get)
    except HTTPError:
        return {"url": None, "title": "Error retrieving latest stories"}

    return articles
