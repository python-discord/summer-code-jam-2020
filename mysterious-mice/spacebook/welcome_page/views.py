from django.shortcuts import render
from django.views.generic import DetailView
from .models import VisitCount


# Create your views here.
class Welcome(DetailView):
    template_name = "welcome_page/welcome.html"

    def get(self, request, *args, **kwargs):
        count = VisitCount.objects.get(id=21)
        count.num_visits += 1
        count.save(update_fields=['num_visits'])

        return render(request, "welcome_page/welcome.html", {"count" : count.num_visits })