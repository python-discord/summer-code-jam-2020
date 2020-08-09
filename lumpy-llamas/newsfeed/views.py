from django.http import JsonResponse
from newsfeed.newsfeed_request import retrieve_articles, get_best_stories, get_new_stories

# url to the hacker-news api to retrieve articles


# function to get the new news from the hackernews API
def get_new_newsfeed(request):
    new_newsfeed = retrieve_articles(get_new_stories(), 5)
    return JsonResponse({'news': new_newsfeed})


# function to get the best news from the hackernews API
def get_best_newsfeed(request):
    best_newsfeed = retrieve_articles(get_best_stories(), 5)
    return JsonResponse({'news': best_newsfeed})
