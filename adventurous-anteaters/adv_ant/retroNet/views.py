from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


# index view when user logs in
def index(request):
    return render(request, 'index.html')


# for registration of a new user
def register(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'index.html')
    context['form'] = form
    return render(request, 'register.html', context)
