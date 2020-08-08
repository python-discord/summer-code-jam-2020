from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
# Renders the home page


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/home.html')


def register(request: HttpRequest) -> HttpResponse:
    """
    If the request is a post request, it saves the form if it's valid.
    If the request is a get request it just simply renders the template
    with a register form.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
