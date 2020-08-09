from django.shortcuts import render


# Create your views here.
def index(request):
    """Views to render the homepage index."""

    context = {
        "login": request.user.is_authenticated,
    }

    if request.user.is_authenticated:
        context["username"] = request.user.username

    return render(request, "home/index.html", context)


def about_us(request):
    """Views to render the About Us page."""

    context = {"login": request.user.is_authenticated, "page": "about_us"}

    return render(request, "home/about.html", context)

def error_404_view(request,exception):
    """Views to render the 404 error page."""

    render (request, '404.html')
