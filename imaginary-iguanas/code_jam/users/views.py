from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserUpdateForm, UserPasswordUpdateForm, ProfileCreateForm, ProfileUpdateForm
from .models import Profile


def home(request):
    return render(request, 'users/home.html')


def signup(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileCreateForm(request.POST, request.FILES)
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
        profile_form = ProfileCreateForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/signup.html', context)


@login_required
def user_settings(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.save()
            messages.success(request, 'Profile updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'profile_form': profile_form}
    return render(request, 'users/settings.html', context)


@login_required
def user_password_update(request):
    if request.method == 'POST':
        password_form = UserPasswordUpdateForm(user=request.user, data=request.POST or None)
        if password_form.is_valid():
            updated_user = password_form.save()
            update_session_auth_hash(request, updated_user)
            messages.success(request, 'Profile updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        password_form = UserPasswordUpdateForm(request.POST)

    context = {'password_form': password_form}
    return render(request, 'users/updatepassword.html', context)


def users(request):
    profiles = Profile.objects.all()
    return render(request, 'users/users.html', {"profiles": profiles, "profile_count": len(profiles)})
