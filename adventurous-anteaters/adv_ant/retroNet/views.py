from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet, UpdateProfile
from .forms import TweetForm, Updateprofile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# index view when user logs in

@login_required(login_url='/login/')
def createpost(request):
    return render(request, 'create_tweet.html')


@login_required(login_url='/login/')
def index(request):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        form.save()
        queryset = Tweet.objects.all()
        return render(request, 'index.html', {"data": queryset})
    else:
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


@login_required(login_url='/login/')
def update_profile(request):
    return render(request, 'temp_test.html')


@login_required(login_url='/login/')
def update_profile_display(request):
    form = Updateprofile(request.POST or None)
    if form.is_valid():
        form.save()
        querysets = UpdateProfile.objects.all()
        # TODO add proper templates in both return
        return render(request, 'index.html', {"data": querysets})
    else:
        querysets = UpdateProfile.objects.all()
        return render(request, 'index.html', {"data": querysets})


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login/')
def my_profile(request):
    queryset = Tweet.objects.all()
    user_name = request.user.username
    return render(request, 'profile.html',
                  {"data": queryset, "user": user_name})


@login_required(login_url='/login/')
def user_profile(request):
    return HttpResponse("Wait for templates")


def logout_page(request):
    return render(request, 'logout.html')


def logout_request(request):
    logout(request)
    return redirect("my_profile")


def account_deletion(request):
    return render(request, 'account_deletion_confirmation.html')


@login_required
def create_tweet(request):
    return render(request, 'create_tweet.html')


@login_required
def view_tweet(request):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        form.save()
        queryset = Tweet.objects.all()
        return render(request, 'view_tweet.html', {"data": queryset})
    else:
        queryset = Tweet.objects.all()
        return render(request, 'view_tweet.html', {"data": queryset})
