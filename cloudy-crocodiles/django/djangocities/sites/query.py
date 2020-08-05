from djangocities.cities.models import City
from djangocities.graphql import query
from djangocities.sites.models import Site
from djangocities.pages.models import Page


@query.field("allSites")
def resolve_all_sites(*_):
    return Site.objects.all()


@query.field("citySites")
def resolve_city_sites(*_, id):
    city = City.objects.get(id=id)
    return Site.objects.filter(city=city)


@query.field("site")
def resolve_site(*_, slug):
    return Site.objects.get(slug=slug)


@query.field("allPages")
def resolve_all_pages(*_):
    return Page.objects.all()


@query.field("page")
def resolve_page(*_, id):
    return Page.objects.get(id=id)
