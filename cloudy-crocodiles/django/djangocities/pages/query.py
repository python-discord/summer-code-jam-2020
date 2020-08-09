from djangocities.graphql import query
from .models import Page


@query.field("allPages")
def resolve_all_pages(root, info):
    return Page.objects.all()


@query.field("page")
def resolve_page(*_, id):
    return Page.objects.get(id=id)
