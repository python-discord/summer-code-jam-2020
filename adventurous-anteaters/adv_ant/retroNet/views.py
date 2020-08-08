from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet
from .forms import *
from django.contrib.auth.decorators import login_required


# index view when user logs in

@login_required(login_url='/login/')
def createpost(request):
    return render(request, 'tweet.html')


@login_required(login_url='/login/')
def index(request):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        form.save()
        queryset = Tweet.objects.all()
        print(queryset)
        return render(request, 'index.html', {"data": queryset})
    else:
        queryset = Tweet.objects.all()
        return render(request, 'index.html',{"data":queryset})


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


def integration(request):
    return render(request, 'title.html')


@login_required(login_url='/login/')
def home(request):
    return HttpResponse("Wait for templates")

@login_required(login_url='/login/')
def my_profile(request):
    return HttpResponse("Wait for templates")

@login_required(login_url='/login/')
def update_profile(request):
    return HttpResponse("Wait for templates")

@login_required(login_url='/login/')
def user_profile(request):
    return HttpResponse("Wait for templates")

@login_required(login_url='/login/')
def delete_profile(request):
    return HttpResponse("Wait for templates")

@login_required(login_url='/login/')
def delete_tweet(request):
    return HttpResponse("Wait for templates")
