from django.shortcuts import render


# Create your views here.
def homepage(request):
    """Views to render the homepage."""

    return render(request, "home.html")

def aboutus(request):
    """ Views to render the About Us page. """
    template = "about.html"
    context = aboutus
    return render(request, template)
