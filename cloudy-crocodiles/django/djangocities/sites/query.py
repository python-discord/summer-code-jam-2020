from djangocities.graphql import query
from djangocities.cities.models import City
from djangocities.sites.models import Site

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
