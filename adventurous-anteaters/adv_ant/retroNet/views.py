from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


def index(request):
    return render(request, 'index.html')


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

# def register(response):
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#
#         return redirect("/login")
#     else:
#         form = RegisterForm()
#     return render(response, "register.html", {"form": form})
