from django.shortcuts import render
from .forms import UserRegisterForm
import typing
from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest) -> HttpResponse:
    """
    Handles feed home GET request
    :param request:
    :return: Feed home with context
    """
    context = {
        'feed': [
            {
                "content": "Hello!"
            },
            {
                "content": "Hello 2!"
            },
        ]
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

    :param request:
    :return:
    """
    return render(request, 'login.html')