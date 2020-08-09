import requests
from decouple import config
from django.shortcuts import render
from users.models import UserPreferences


def main(request):
    news_key = config('NEWS_KEY')
    url = 'https://api.nytimes.com/svc/topstories/v2/us.json?api-key=' + news_key
    nyt_usnews = requests.get(url).json()
    nyt_usnews_list = []

    for top_story in range(0, 4):
        nyt_usnews_list.append(
            {'title': nyt_usnews['results'][top_story]['title'],
             'abstract': nyt_usnews['results'][top_story]['abstract'],
             'url': nyt_usnews['results'][top_story]['url'],
             'img_small': nyt_usnews['results'][top_story]['multimedia'][0]['url']
             }
        )

    context = {
        'news': nyt_usnews_list,
    }

    if request.user.is_authenticated:
        context.update(
            {
                'pref': UserPreferences.objects.get(user=request.user)
            }
        )
        return render(request, 'main/dashboard.html', context)
    return render(request, 'main/dashboard.html', context)


def about(request):
    return render(request, 'main/main-about.html')
