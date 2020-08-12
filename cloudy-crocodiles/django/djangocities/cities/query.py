from djangocities.graphql import query
from djangocities.cities.models import City


@query.field("allCities")
def resolve_all_cities(root, info):
    return City.objects.all()


@query.field("city")
def resolve_city(*_, slug):
    return City.objects.get(slug=slug)
