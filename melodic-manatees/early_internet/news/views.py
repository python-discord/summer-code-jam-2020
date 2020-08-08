from django.shortcuts import render, HttpResponse
from decouple import config
import requests


def news_feed(request):
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
             })

    context = {
               'nyt_us': nyt_usnews_list[0],
               'nyt_us2': nyt_usnews_list[1],
               'nyt_us3': nyt_usnews_list[2],
               'nyt_us4': nyt_usnews_list[3],
               }
    return render(request, 'news/news.html', context)
