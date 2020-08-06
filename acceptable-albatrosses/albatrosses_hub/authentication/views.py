from django.shortcuts import render
from .forms import RegisterForm


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

    return render(request, "login.html")


def logout_page(request):
    """ Views to render the logout page. """

    return render(request, "logout.html")
