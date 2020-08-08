from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account {email} has been created! You can log in now.')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {'user_form': user_form}

    return render(request, 'account/profile.html', context)
