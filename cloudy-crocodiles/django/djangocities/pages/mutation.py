import logging

from djangocities.iam.jwt import load_user
from djangocities.pages.models import Page
from djangocities.sites.models import Site


def resolve_create_page(_, info, data):
    user = load_user(info)
    if not user.is_authenticated:
        raise Exception("You can't do that!")

    site = data.get("site", None)
    version = data.get("version", None)
    content = data.get("content", None)
    file_name = data.get("file_name", None)

    if not site:
        logging.debug("Site is missing")
        raise Exception("Site is missing")
    if not version:
        logging.debug("Version is missing")
        raise Exception("Version is missing")
    if not content:
        logging.debug("Content is missing")
        raise Exception("Content is missing")
    if not file_name:
        logging.debug("File Name is missing")
        raise Exception("File Name is missing")

    try:
        site_obj = Site.objects.get(id=site, user=user)
    except Site.DoesNotExist:
        logging.debug("Site not found")
        raise Exception("Site not found")

    page = Page.objects.create(
        site=site_obj, version=version, content=content, file_name=file_name
    )

    return page


def resolve_update_page(_, info, page_id, data):
    user = load_user(info)
    if not user.is_authenticated:
        raise Exception("You can't do that!")

    try:
        page = Page.objects.get(id=page_id, site__user=user)
    except Page.DoesNotExist:
        logging.debug("Page not found")
        raise Exception("Page not found")

    site = data.get("site", None)
    try:
        site_obj = Site.objects.get(id=site, user=user)
    except Site.DoesNotExist:
        logging.debug("Site not found")
        raise Exception("Site not found")

    version = data.get("version", None)
    content = data.get("content", None)
    file_name = data.get("file_name", None)

    if site:
        page.site = site_obj
    if version:
        page.version = version
    if content:
        page.content = content
    if file_name:
        page.file_name = file_name

    page.save()
    return page
