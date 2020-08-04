import hashlib
import os
import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from users.forms import RegistrationForm
from users.models import File


def index(request):
    return render(request, 'users/index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.save())
            messages.success(request, 'You are successfully registered')
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'users/login.html')


@login_required(login_url='/login/')
def dashboard(request):
    context = {}
    file = File.objects.filter(user=request.user)
    context = {'file': file}
    return render(request, 'users/dashboard.html', context)


@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return render(request, 'users/logout.html')
