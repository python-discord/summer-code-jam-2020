from ariadne import ObjectType
from djangocities.pages.models import Page

site = ObjectType("Site")


@site.field("pages")
def resolve_pages(obj, info):
    return obj.page_set.all()


@site.field("default_page")
def resolve_default_page(obj, info):
    DEFAULT_FILE_NAME = "index.html"
    pages = obj.page_set.filter(site=obj).values_list("file_name", flat=True)

    if len(pages) == 0:
        return ""
    if DEFAULT_FILE_NAME in pages:
        return DEFAULT_FILE_NAME

    return pages[0]
