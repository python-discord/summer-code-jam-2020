from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    """
    This view asks new users to sign up.
    (Registers new accounts)

    """
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'users/signup.html', {'form': form})
