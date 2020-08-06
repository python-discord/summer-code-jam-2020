from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/home.html')


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success('Successfully registered!')
            return redirect(request, 'login')
        else:
            return render(request, 'users/register.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
