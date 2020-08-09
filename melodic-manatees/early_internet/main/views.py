from django.shortcuts import render
from users.models import UserPreferences
import requests
from decouple import config


def main(request):
    weather_key = config('WEATHER_KEY')

    # THIS IS WHERE I AM HAVING PROBLEMS CALLING THE PREFERENCES!!!!!!!!!!!

    # city_name = getattr(UserPreferences, 'city_name')
    # country_name = getattr(UserPreferences, 'country_name')
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
          'london' + ',' + 'uk' + '&appid=' + weather_key + '&units=metric'
    # THESE CITIES SHOULD NOT BE HARDCODED

    city_weather = requests.get(url).json()

    weather_dict = {'city': city_weather['name'],
                    'country': city_weather['sys']['country'],
                    'temperature': city_weather['main']['temp'],
                    'description': city_weather['weather'][0]['description']
                    }

    context = {'weather': weather_dict}


    if request.user.is_authenticated:
        context = {
            'pref': UserPreferences.objects.get(user=request.user),
            'weather': weather_dict,
        }
        return render(request, 'main/dashboard.html', context)

    return render(request, 'main/dashboard.html', context)


def about(request):
    return render(request, 'main/main-about.html')
