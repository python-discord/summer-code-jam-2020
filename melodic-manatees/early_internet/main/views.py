from django.shortcuts import render
from users.models import UserProfile


def main(request):
    background = UserProfile.background_image
    not_default_background = UserProfile.not_default_background
    return render(request, 'main/main-base.html', {'background':background, 'not_default_background':not_default_background})


def about(request):
    return render(request, 'main/main-about.html')
