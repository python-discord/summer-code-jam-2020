from django.shortcuts import render


# Create your views here.
def register_page(request):
    """ Views to render the register page. """

    return render(request, "register.html")
