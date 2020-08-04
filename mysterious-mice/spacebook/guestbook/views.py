from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import Guestbook
from .models import Guestbook as GbModel


def guestbook(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Guestbook(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print("======1===============")
            print(request.POST["author"])
            GbModel.objects.create(
                author=request.POST["author"],
                text=request.POST["text"],
                email=request.POST["email"],
                published_date=timezone.now(),
            )
            print("======2===============")
            # GbModel.publish()
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Guestbook()

    comments = GbModel.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(
        request, "guestbook/guestbook.html", {"form": form, "comments": comments}
    )
