from djangocities.cities.models import City
from djangocities.graphql import query
from djangocities.sites.models import Site
from djangocities.pages.models import Page
from djangocities.folders.models import Folder
from djangocities.iam.jwt import load_user


@query.field("allSites")
def resolve_all_sites(*_):
    return Site.objects.all()


@query.field("site")
def resolve_site(*_, id):
    return Site.objects.get(id=id)

@query.field("siteFolder")
def resolve_city_site(*_, id, path):
    site = Site.objects.get(id=id)
    return Folder.objects.get(site=site, path=path)


@query.field("citySites")
def resolve_city_sites(*_, id):
    city = City.objects.get(id=id)
    return Site.objects.filter(city=city)


@query.field("citySite")
def resolve_city_site(*_, slug, address):
    city = City.objects.get(slug=slug)
    return Site.objects.get(city=city, address=address)


@query.field("allPages")
def resolve_all_pages(*_):
    return Page.objects.all()


@query.field("page")
def resolve_page(*_, id):
    return Page.objects.get(id=id)

@query.field("userOwnSites")
def resolve_user_own_sites(root, info):
    request = info.context["request"]
    user = load_user(info)
    if not user.is_authenticated:
        raise Exception("You can't do that!")
    return user.site_set.all()
