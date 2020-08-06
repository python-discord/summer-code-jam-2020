from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet


# index view when user logs in

def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Tweet()
            post.content = request.POST.get('content')
            post.save()
            return render(request, 'index.html')
    else:
        return render(request, 'tweet.html')


def index(request):
    queryset = Tweet.objects.all()
    return render(request, 'index.html', {"data": queryset})


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
