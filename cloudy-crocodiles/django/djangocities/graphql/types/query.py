from ariadne import QueryType

from djangocities.user.models import CustomUser as User
from djangocities.cities.models import City

query = QueryType()

@query.field("allUsers")
def resolve_all_users(root, info):
    return User.objects.all()

@query.field("allCities")
def resolve_all_cities(root, info):
    return City.objects.all()
