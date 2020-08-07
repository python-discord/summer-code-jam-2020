from django.shortcuts import render


# Create your views here.
def homepage(request):
    """Views to render the homepage."""

    return render(request, "home.html")
