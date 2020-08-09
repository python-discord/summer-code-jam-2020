import requests
from requests.exceptions import HTTPError


# function to test the connectivity to the API. Returns True if the request is valid
def test_api_connection(url_api):
    try:
        response = requests.get(f'{url_api}')
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP Error occurred: {http_err}')
    except Exception as err:
        print(f'HTTP Error occurred: {err}')
    else:
        return True


# Function to get the new stories from the API, the output of this is a list with numbers
# each number represents a new story, there are maximum 500 newstories
def get_new_stories(url_api) -> list:
    # newstories.json? refers to the new stories in the API
    if test_api_connection(url_api):
        response = requests.get(f'{url_api}newstories.json?')
        return response.json()


# Function to get the best stories from the API, the output of this is a list with numbers
# each number represents a top story, there are maximum 500 best stories
def get_best_stories(url_api) -> list:
    # beststories.json? refers to the best stories in the API
    if test_api_connection(url_api):
        response = requests.get(f'{url_api}beststories.json?')
        return response.json()


# Function to retrieve the articles, this can either be the new stories or the best stories
# the output of this function depends on the input of the arguments
def retrieve_articles(url_api, stories_list, number_articles):
    # define an empty list and set index to 0
    articles = []
    index = 0
    # avoid out of range value for number_articles (our max is 5)
    if number_articles > 5:
        number_articles = 5

    # iterating trough the required number of articles
    # if an article has no url, the next available article with url is taken
    # the articles are appended one by one to a list
    if test_api_connection(url_api):
        while index < number_articles:
            api_response = requests.get(f'{url_api}item/{stories_list[index]}.json').json()
            if api_response.get("url") is not None:
                filtered_dict = {
                    "url": api_response.get("url"),
                    "title": api_response.get("title")
                }
                articles.append(dict(filtered_dict))
                index += 1
            else:
                index += 1
                number_articles += 1
    else:
        return {"url": None, "title": "Error retrieving latest stories"}

    return articles
