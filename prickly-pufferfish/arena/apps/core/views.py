from django.shortcuts import render
from django.http import HttpResponse

<<<<<<< HEAD
def index(request):
    return HttpResponse("It works!")
=======
# Create your views here.


def index(request):
    return render(request, "base.html")
>>>>>>> 4ca44e200af1b2431376b2ea67d91fd5815cd219
