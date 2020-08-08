from django.shortcuts import render


# Create your views here.
def homepage(request):
    """Views to render the homepage."""

    context = {
        "login" : False,
    }

    if "email" in request.session:
        context["username"] = request.session["username"]
        context["login"] = True

    return render(request, "home.html", context)

def about_us(request):
    """Views to render the About Us page."""
    
    return render(request, "about.html")
