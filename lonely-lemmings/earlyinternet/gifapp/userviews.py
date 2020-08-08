import typing

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Project
from .forms import UserRegisterForm


def home(request: HttpRequest) -> HttpResponse:
    """
    Handles feed home GET request
    :param request:
    :return: Feed home with context
    """
    context = {
        "feed": Project.objects.all()
    }
    return render(request, 'home.html', context)


def register(request: HttpRequest) -> HttpResponse:
    """
    Handles register endpoint POST request
    :param request: HttpRequest object containing form data for registering a new user
    :return: redirect if successful account formation, else the same RegisterForm
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('feed-home')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', { 'form': form })


def login(request: HttpRequest) -> HttpResponse:
    """
    Handles login request
    :param request:
    :return:
    """
    return render(request, 'login.html')


def profile(request: HttpRequest) -> HttpResponse:

    return render(request, 'profile.html', context)


class PostListView(ListView):
    model =