from django.shortcuts import render
from users.models import UserPreferences
from diary.models import DiaryEntry


def main(request):
    if request.user.is_authenticated:
        context = {
            'pref': UserPreferences.objects.get(user=request.user),
            'entries': DiaryEntry.objects.get(user=request.user)
        }
        return render(request, 'main/dashboard.html', context)
    return render(request, 'main/dashboard.html')


def about(request):
    return render(request, 'main/main-about.html')
