from django.http import HttpResponse
from djangocities.cities.models import City
from .models import Site
from djangocities.pages.models import Page


def index(request, slug, address, page):
    city = City.objects.get(slug=slug)
    site = Site.objects.get(city=city, address=address)
    page = Page.objects.get(site=site, file_name=page)
    html = page.content
    return HttpResponse(html)
