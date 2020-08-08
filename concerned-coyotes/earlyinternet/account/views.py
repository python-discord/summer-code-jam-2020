from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm


def register(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("index", permanent=True)

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        # Check if form is valid
        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            new_user.set_password(
                user_form.cleaned_data['password'])

            new_user.save()

            return redirect("login", permanent=True)
    else:
        user_form = UserRegistrationForm()

    return render(request,
                  'register.html',
                  {'form': user_form})


@login_required
def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)

    return redirect("login", permanent=True)
