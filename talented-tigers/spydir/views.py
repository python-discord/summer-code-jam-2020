from django.shortcuts import render
from django.http import HttpResponse
from .models import GeneratedPage
from . import generate_page


def homepage(request):
    lengths = [
        len(GeneratedPage.objects.filter(page_type="INFO")),
        len(GeneratedPage.objects.filter(page_type="INFO")),
        len(GeneratedPage.objects.filter(page_type="INFO")),
        len(GeneratedPage.objects.filter(page_type="INFO")),
    ]
    max_length = max(lengths)
    print(max_length)

    ctx = { #Leave all types as `INFO` for now as there are no other populated types
        'BIZ':  GeneratedPage.objects.filter(page_type="INFO"),
        'BLOG': GeneratedPage.objects.filter(page_type="INFO"),
        'FOOD': GeneratedPage.objects.filter(page_type="INFO"),
        'INFO': GeneratedPage.objects.filter(page_type="INFO"),
                
        'BIZ_LENGTH':  lengths[0],
        'BLOG_LENGTH': lengths[1],
        'FOOD_LENGTH': lengths[2],
        'INFO_LENGTH': lengths[3],
        'MAX_LENGTH': max_length,
    } 

    

    return render(request, "spydir/home.html", ctx)


def load_generated_page(request, page_name):
    """Loads either an already generated page or generates one and loads it"""
    page = None
    try:
        page = GeneratedPage.objects.get(page_title=page_name)
        if(page.is_generated == False):
            page = generate_page.generate_page(page_name)
    except GeneratedPage.DoesNotExist:
        return render(request, "spydir/404.html")

    ctx = {
        'page': page
    }
    if page.page_type == "SCAM":
        return render(request, f"spydir/generators/scams/{page.scam_type}.html", context=ctx)
    return render(request, f"spydir/generators/{page.page_type}.html", context=ctx)
