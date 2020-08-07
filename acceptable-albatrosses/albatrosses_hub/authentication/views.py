from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import HubUser


# Create your views here.
def register_page(request):
    """Views to render the register page."""

    form = RegisterForm(request.POST or None)
    context = {
        'form' : form,
        'error_message' : "",
    }

    if request.method == "POST":
        if form.is_valid():
            if request.POST["password"] != request.POST["re_password"]:
                context["error_message"] = "Password is not same"
            
            else:
                user_data = HubUser()
                user_data.process(form)
                user_data.save()

                return redirect("login_page")

    return render(request, "register.html", context)


def login_page(request):
    """Views to render the login page."""

    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }

    return render(request, "login.html", context)


def logout_page(request):
    """Views to render the logout page."""

    return render(request, "logout.html")
