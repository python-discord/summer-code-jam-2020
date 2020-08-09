import requests
from decouple import config
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from users.models import UserPreferences
from diary.models import DiaryEntry
from diary.forms import DiaryEntryForm


def main(request):

    news_key = config('NEWS_KEY')
    weather_key = config('WEATHER_KEY')

    news_url = 'https://api.nytimes.com/svc/topstories/v2/us.json?api-key=' + news_key
    nyt_usnews = requests.get(news_url).json()
    nyt_usnews_list = []

    for top_story in range(0, 4):
        nyt_usnews_list.append(
            {
                'title': nyt_usnews['results'][top_story]['title'],
                'abstract': nyt_usnews['results'][top_story]['abstract'],
                'url': nyt_usnews['results'][top_story]['url'],
                'img_small': nyt_usnews['results'][top_story]['multimedia'][0]['url']
             }
        )

    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
        'london' + ',' + 'uk' + '&appid=' + weather_key + '&units=metric'

    if request.user.is_authenticated:

        try:
            entries = DiaryEntry.objects.filter(creator=request.user)
        except ObjectDoesNotExist:
            entries = None

        if request.method == 'POST':
            form = DiaryEntryForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.creator = request.user
                instance.save()
                return redirect('/')
        else:
            form = DiaryEntryForm()

        pref = UserPreferences.objects.get(user=request.user)

        weather_url = 'https://api.openweathermap.org/data/2.5/weather?q='\
            f'{pref.city_name},{pref.country_name}&appid={weather_key}&units=metric'

        city_weather = requests.get(weather_url).json()
        weather_dict = {
            'city': city_weather['name'],
            'country': city_weather['sys']['country'],
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description']
        }

        context = {
            'pref': pref,
            'news': nyt_usnews_list,
            'weather': weather_dict,
            'entries': entries,
            'form': form
        }
        return render(request, 'main/dashboard.html', context)

    city_weather = requests.get(weather_url).json()

    weather_dict = {'city': city_weather['name'],
                    'country': city_weather['sys']['country'],
                    'temperature': city_weather['main']['temp'],
                    'description': city_weather['weather'][0]['description']
                    }

    context = {
        'news': nyt_usnews_list,
        'weather': weather_dict,
    }
    return render(request, 'main/dashboard.html', context)
