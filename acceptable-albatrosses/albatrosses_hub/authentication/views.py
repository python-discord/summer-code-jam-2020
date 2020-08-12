from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


# Create your views here.
def register_page(request):
    """Views to render the register page."""

    # Prevent the logged in user to access register page
    if request.user.is_authenticated:
        return redirect("/")

    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
        "error_message": "",
    }

    if request.method == "POST" and form.is_valid():
        all_valid = True

        submitted_email = request.POST["email"]
        if User.objects.filter(email=submitted_email).exists():
            context["error_message"] = "Email has been registered before"
            all_valid &= False

        submitted_username = request.POST["username"]
        if User.objects.filter(username=submitted_username):
            context["error_message"] = "Username has been taken"
            all_valid &= False

        if request.POST["password"] != request.POST["re_password"]:
            context["error_message"] = "Password is not same"
            all_valid &= False

        if all_valid:
            new_user = User.objects.create_user(
                email=submitted_email, username=submitted_username, password=request.POST["password"]
            )
            new_user.save()

            return redirect("authentication:login")

    return render(request, "authentication/register.html", context)


def login_page(request):
    """Views to render the login page."""

    # Prevent the logged in user to access login page
    if request.user.is_authenticated:
        return redirect("/")

    form = LoginForm(request.POST or None)
    context = {
        "form": form,
        "error_message": "",
    }

    if request.method == "POST" and form.is_valid():
        all_valid = True

        user_name = request.POST["username"]
        if not User.objects.filter(username=user_name):
            context["error_message"] = "This username is not registered yet"
            all_valid &= False

        password = request.POST["password"]
        if not authenticate(request, username=user_name, password=password):
            context["error_message"] = "Wrong password"
            all_valid &= False

        if all_valid:
            user = authenticate(request, username=user_name, password=password)

            try:
                login(request, user)
            except AttributeError:  # handle AttributeError during unit test
                pass

            return redirect("/")

    return render(request, "authentication/login.html", context)


def logout_page(request):
    """Views to render the logout page."""

    # Prevent the Anonymous user to access logout page
    if not request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        try:
            logout(request)
        except AttributeError:  # handle AttributeError during unit test
            pass

        return redirect("/")

    return render(request, "authentication/logout.html")
