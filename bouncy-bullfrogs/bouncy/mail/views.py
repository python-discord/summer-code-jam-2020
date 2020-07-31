from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, "mail/inbox.html")
    else:
        return HttpResponseRedirect(reverse("login"))
