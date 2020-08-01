from django.shortcuts import render
from django.views.generic import ListView
from .models import Thread, ThreadMessage
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse


class ThreadListView(ListView):
    model = Thread
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ThreadView(ListView):
    model = ThreadMessage
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")