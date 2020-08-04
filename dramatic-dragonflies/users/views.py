from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.core.handlers.asgi import ASGIRequest
from django.http.response import HttpResponse
# Create your views here.


def home(request: ASGIRequest) -> HttpResponse:
    return render(request, 'users/home.html')


def register(request: ASGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'users/register.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
