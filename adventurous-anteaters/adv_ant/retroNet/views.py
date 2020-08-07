from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet
from  .forms import *


# index view when user logs in

def createpost(request):
    return render(request, 'tweet.html')


def index(request):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        form.save()
        queryset = Tweet.objects.all()
        print(queryset)
        return render(request, 'index.html', {"data": queryset})
    # queryset = Tweet.objects.all()


# for registration of a new user
def register(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'tweet.html')
    context['form'] = form
    return render(request, 'register.html', context)
