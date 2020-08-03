from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserCreateForm, ProfileCreateForm


def home(request):
    return render(request, 'users/home.html')


def signup(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        profile_form = ProfileCreateForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            messages.success(request, 'Account created! You can now login')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserCreateForm()
        profile_form = ProfileCreateForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/signup.html', context)
