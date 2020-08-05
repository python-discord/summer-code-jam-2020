from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserUpdateForm, ProfileUpdateForm


def home(request):
    return render(request, 'users/home.html')


def signup(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            messages.success(request, 'Account created! You can now login')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/signup.html', context)


# @login_required
def user_settings(request):
    if request.method == 'POST':
        # user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.profile)
        if profile_form.is_valid():
            # updated_user = user_form.save()
            profile = profile_form.save(commit=False)
            # profile.user = updated_user
            profile.save()
            messages.success(request, 'Profile updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        # user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()

    context = {'profile_form': profile_form}
    return render(request, 'users/settings.html', context)
