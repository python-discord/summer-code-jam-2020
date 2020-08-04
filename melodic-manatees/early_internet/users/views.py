from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .forms import UserRegistrationForm, UserPreferencesForm
from.models import UserPreferences

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    session = UserPreferences.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserPreferencesForm(instance=session, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Preferences Updated!')
            return redirect('profile')
    else:
        form = UserPreferencesForm()

    context = {
        'pref': UserPreferences.objects.get(user=request.user),
        'form': form
    }
    return render(request, 'users/profile.html', context)


def user_logout(request):
    messages.info(request, 'You have been logged out')
    return LogoutView.as_view(template_name='main/main-base')(request)
