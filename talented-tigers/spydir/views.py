from django.shortcuts import render
from django.http import HttpResponse
from .models import GeneratedPage
from . import generate_page


def homepage(request):
    return render(request, "spydir/home.html")


def load_generated_page(request, page_name):
    """Loads either an already generated page or generates one and loads it"""
    page = None
    try:
        page = GeneratedPage.objects.get(page_title=page_name)
    except GeneratedPage.DoesNotExist:
        page = generate_page.generate_page(page_name)

    ctx = {
        'page': page
    }
    if page.page_type == "SCAM":
        return render(request, f"spydir/generators/scams/{page.scam_type}.html", context=ctx)
    return render(request, f"spydir/generators/{page.page_type}.html", context=ctx)
