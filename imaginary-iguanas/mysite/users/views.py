import pycountry
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import UserProfile
from .forms import UserCreateForm, ProfileCreateForm
from .forms import MySiteUserCreationForm, MySiteUserProfileSettingsForm


class SignUpView(CreateView):
    form_class = MySiteUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


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


# @login_required
def user_settings(request):

    '''
        if request.method == 'POST':
        update_form = MySiteUserProfileSettingsForm(request.POST, request.FILES, instance=request.user)
        if update_form.isvalid():
            update_form.save()
            messages.success(request, f'Your profile has been updated successfully :)')
            return redirect('profile')
    else:
        update_form = MySiteUserProfileSettingsForm(instance=request.user)
    '''
    update_form = MySiteUserProfileSettingsForm()

    context = {
        'update_form': update_form
    }
    return render(request, 'settings.html', context)
