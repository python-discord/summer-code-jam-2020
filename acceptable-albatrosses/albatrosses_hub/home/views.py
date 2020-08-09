from django.shortcuts import render


# Create your views here.
def homepage(request):
    """Views to render the homepage."""

    context = {
        "login": request.user.is_authenticated,
    }

    if request.user.is_authenticated:
        context["username"] = request.user.username

    return render(request, "home.html", context)

def about_us(request):
    """Views to render the About Us page."""

    context = {
        "login": request.user.is_authenticated
    }

    return render(request, "about.html", context)
