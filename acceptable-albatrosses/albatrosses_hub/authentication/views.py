from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import HubUser


# Create your views here.
def register_page(request):
    """Views to render the register page."""

    form = RegisterForm(request.POST or None)
    context = {
        "form" : form,
        "error_message" : "",
    }

    if request.method == "POST" and form.is_valid():
        all_valid = True

        submitted_email = request.POST["email"]
        if HubUser.objects.filter(pk=submitted_email).exists():
            context["error_message"] = "Email has been registered before"
            all_valid &= False

        submitted_username = request.POST["username"]
        if HubUser.objects.filter(username__icontains=submitted_username):
            context["error_message"] = "Username has been taken"
            all_valid &= False

        if request.POST["password"] != request.POST["re_password"]:
            context["error_message"] = "Password is not same"
            all_valid &= False

        if all_valid:
            user_data = HubUser()
            user_data.process(form)
            user_data.save()

            return redirect("login_page")

    return render(request, "register.html", context)


def login_page(request):
    """Views to render the login page."""

    form = LoginForm(request.POST or None)
    context = {
        "form": form,
        "error_message" : "",
    }

    if request.method == "POST" and form.is_valid():
        all_valid = True

        submitted_email = request.POST["email"]
        if not HubUser.objects.filter(pk=submitted_email).exists():
            context["error_message"] = "This email is not registered yet"
            all_valid &= False

        submitted_password = request.POST["password"]
        query = HubUser.objects.filter(email=submitted_email).values("email", "password")
        hashed_password = query[0]["password"]
        if not check_password(submitted_password, hashed_password):
            context["error_message"] = "Wrong password"
            all_valid &= False

        if all_valid:
            query = HubUser.objects.filter(email=submitted_email).values("username")
            request.session["email"] = submitted_email
            request.session["username"] = query[0]["username"]
            request.session.set_expiry(0)

            return redirect("/")

    return render(request, "login.html", context)


def logout_page(request):
    """Views to render the logout page."""

    return render(request, "logout.html")
