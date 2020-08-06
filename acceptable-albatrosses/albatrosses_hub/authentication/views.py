from django.shortcuts import render


# Create your views here.
def register_page(request):
    """ Views to render the register page. """

    return render(request, "register.html")


def login_page(request):
    """ Views to render the login page. """

    return render(request, "login.html")


def logout_page(request):
    """ Views to render the logout page. """

    return render(request, "logout.html")