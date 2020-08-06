from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import UserRegisterForm


def register(request):
    """Saves the form if valid, registering the user. Otherwise, form must be repeated."""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "core/register.html", {"form": form})
