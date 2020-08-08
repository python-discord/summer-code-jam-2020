from django.shortcuts import render
from django.views.generic import View
from .services import get_current_weather, get_week_weather


class CurrentWeatherView(View):
    """
    Provides the weather on Mars for the current Sol (Mars Day).
    """

    def get(self, request):
        context = get_current_weather(request)
        return render(request, "mars_weather/current_weather.html", context)


class WeekWeatherView(View):
    """
    Provides details regarding the weather the past week on Mars.
    """

    def get(self, request):
        context = get_week_weather(request)
        return render(request, "mars_weather/week_weather.html", context)
