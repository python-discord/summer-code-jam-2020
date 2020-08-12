from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Account created for %s." % username)
            return redirect("login_view")
        else:
            messages.error(request, "Account creation failed.")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return redirect("homepage")
