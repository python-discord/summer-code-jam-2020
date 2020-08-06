from django.shortcuts import render
from .forms import RegisterForm, LoginForm


# Create your views here.
def register_page(request):
    """ Views to render the register page. """

    form = RegisterForm(request.POST or None)
    context = {
        'form' : form,
    }

    return render(request, "register.html", context)


def login_page(request):
    """ Views to render the login page. """

    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }

    return render(request, "login.html", context)


def logout_page(request):
    """ Views to render the logout page. """

    return render(request, "logout.html")
