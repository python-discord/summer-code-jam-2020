from django.http import JsonResponse
from newsfeed.newsfeed_request import retrieve_articles, get_best_stories, get_new_stories

# url to the hacker-news api to retrieve articles
url = 'https://hacker-news.firebaseio.com/v0/'


def get_new_newsfeed(request):
    new_newsfeed = retrieve_articles(url, get_new_stories(url), 5)
    return JsonResponse({'new_news': new_newsfeed})


def get_best_newsfeed(request):
    best_newsfeed = retrieve_articles(url, get_best_stories(url), 5)
    return JsonResponse({'best_news': best_newsfeed})
