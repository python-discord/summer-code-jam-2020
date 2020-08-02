from ariadne import QueryType

from djangocities.cities.models import City

query = QueryType()


@query.field("allCities")
def resolve_all_cities(root, info):
    return City.objects.all()
