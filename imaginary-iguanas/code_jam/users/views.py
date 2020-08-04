from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserUpdateForm, ProfileUpdateForm


def home(request):
    return render(request, 'users/home.html')


def signup(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST)
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
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/signup.html', context)


# @login_required
def user_settings(request):
    """
    if request.method == 'POST':
    update_form = MySiteUserProfileSettingsForm(request.POST, request.FILES, instance=request.user)
    if update_form.isvalid():
        update_form.save()
        messages.success(request, f'Your profile has been updated successfully :)')
        return redirect('profile')
    else:
        update_form = MySiteUserProfileSettingsForm(instance=request.user)
    """
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/settings.html', context)
