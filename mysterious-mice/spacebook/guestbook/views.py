from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView
from .forms import Guestbook
from .models import Guestbook as GbModel


class Guestbook(DetailView):
    template_name = "guestbook/guestbook.html"
    form_class= Guestbook
    initial = {'key': 'value'}

    def post(self, request, *args, **kwargs):
        # create a form instance and populate it with data from the request:
        form = self.form_class(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #create a model with the request data
            GbModel.objects.create(
                author=request.POST["author"],
                text=request.POST["text"],
                email=request.POST["email"],
                published_date=timezone.now(),
            )

        comments = GbModel.objects.filter(published_date__lte=timezone.now()).order_by(
                "published_date"
                )

        return render(
            request, self.template_name, {"form": form, "comments": comments}
        )

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        comments = GbModel.objects.filter(published_date__lte=timezone.now()).order_by(
                "published_date"
                )
        return render(request, self.template_name, {"form": form, "comments": comments})

