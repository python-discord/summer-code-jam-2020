from djangocities.graphql import query
from .models import Image

@query.field("allImages")
def resolve_all_images(root, info):
    return Image.objects.all()

@query.field("image")
def resolve_image(*_, id):
    return Image.objects.get(id=id)
