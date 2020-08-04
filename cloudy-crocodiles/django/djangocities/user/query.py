from djangocities.graphql import query
from djangocities.user.models import CustomUser as User


@query.field("allUsers")
def resolve_all_users(root, info):
    return User.objects.all()
