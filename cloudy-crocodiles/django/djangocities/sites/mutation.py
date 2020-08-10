import logging

from djangocities.cities.models import City
from djangocities.iam.jwt import load_user
from djangocities.pages.models import Page
from djangocities.sites.models import Site


def create_default_page(site):
    page = Page.objects.create(site=site, file_name="index.html")
    return page


def resolve_create_site(_, info, data):
    user = load_user(info)
    if not user.is_authenticated:
        raise Exception("You can't do that!")

    city = data.get("city", None)
    description = data.get("description", None)

    if not city:
        logging.debug("City is missing")
        raise Exception("City is missing")
    if not description:
        logging.debug("Description is missing")
        raise Exception("Description is missing")

    try:
        city_obj = City.objects.get(id=city)
    except City.DoesNotExist:
        logging.debug("City not found")
        raise Exception("City not found")

    site = Site.objects.create(city=city_obj, description=description, user=user)
    create_default_page(site)

    return site


def resolve_update_site(_, info, site_id, data):
    user = load_user(info)
    if not user.is_authenticated:
        raise Exception("You can't do that!")

    try:
        site = Site.objects.get(id=site_id, user=user)
    except Site.DoesNotExist:
        logging.debug("Site not found")
        raise Exception("Site not found")

    city = data.get("city", None)
    description = data.get("description", None)

    if city:
        try:
            city_obj = City.objects.get(id=city)
        except City.DoesNotExist:
            logging.debug("City not found")
            raise Exception("City not found")
        site.city = city_obj

    if description:
        site.description = description

    site.save()
    return site
