from django.shortcuts import render
from users.models import UserPreferences
from news.views import news_feed


def main(request):
    if request.user.is_authenticated:
        # MAYBE MOVE NEWS VIEW INTO HERE
        # news_data = news_feed(request)
        context = {
            'pref': UserPreferences.objects.get(user=request.user)
        }
        return render(request, 'main/dashboard.html', context)
    return render(request, 'main/dashboard.html')


def about(request):
    return render(request, 'main/main-about.html')
