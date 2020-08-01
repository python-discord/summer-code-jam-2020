from django.shortcuts import render
from django.http import HttpResponse
from .models import GeneratedPage


def homepage(request):
    return render(request, 'spydir/home.html')

def info_view(request):
    return render(request, 'spydir/generators/info.html')

def load_generated_page(request, pagename):
    """Loads either an already generated page or generates one and loads it"""

    try:
        page = GeneratedPage.objects.get(page_title=pagename)
    except GeneratedPage.DoesNotExist:
        #generate_page(pagename)
        #page = GeneratedPage.objects.get(page_title=pagename)
        page = None

    response = "<h1>This page would be about {0}.</h1>".format(pagename)
    return HttpResponse(response)
