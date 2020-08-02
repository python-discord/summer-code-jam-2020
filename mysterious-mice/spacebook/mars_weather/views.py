from django.shortcuts import render
from django.views.generic import View
from .services import get_current_weather

# Create your views here.


class CurrentWeatherView(View):
    """
    Provides the weather on Mars for the current Sol (Mars Day).

    If user reloads the page, used cached data instead of making call to API again.
    """

    template_name = "mars_weather/weather.html"

    def get(self, request):
        context = get_current_weather(request)
        return render(request, "mars_weather/weather.html", context)
