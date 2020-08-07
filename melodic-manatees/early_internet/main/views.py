from django.shortcuts import render
from users.models import UserProfile


def main(request):
    background = UserProfile.background_image
    return render(request, 'main/main-base.html', {'background': background})




def about(request):
    return render(request, 'main/main-about.html')
