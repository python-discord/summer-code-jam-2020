from django.shortcuts import render
from .models import GeneratedPage
from .generate_page import generate_page, authorize_page


def homepage(request):

    lengths = [
        len(GeneratedPage.objects.filter(page_type="BLOG")),
        len(GeneratedPage.objects.filter(page_type="INFO")),
        len(GeneratedPage.objects.filter(page_type="BIZ")),
    ]
    max_length = max(lengths)
    print(max_length)

    ctx = {  # Leave all types as `INFO` for now as there are no other populated types
        "BLOG": GeneratedPage.objects.filter(page_type="BLOG"),
        "INFO": GeneratedPage.objects.filter(page_type="INFO"),
        "BIZ": GeneratedPage.objects.filter(page_type="BIZ"),
        "BLOG_LENGTH": lengths[0],
        "INFO_LENGTH": lengths[1],
        "BIZ_LENGTH": lengths[2],
        "MAX_LENGTH": max_length,
    }

    return render(request, "spydir/home.html", ctx)


def load_generated_page(request, page_name):
    """Loads either an already generated page or generates one and loads it"""
    page = None
    try:
        page = GeneratedPage.objects.get(page_title=page_name)
        if not page.is_generated:
            page = generate_page(page_name)
    except GeneratedPage.DoesNotExist:
        return render(request, "spydir/404.html")

    ctx = {"page": page}

    return render(request, f"spydir/generators/{page.page_type}.html", context=ctx)
