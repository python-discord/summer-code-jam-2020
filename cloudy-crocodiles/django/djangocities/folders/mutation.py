import logging

from djangocities.folders.models import Folder
from djangocities.iam.jwt import load_user
from djangocities.sites.models import Site


def resolve_create_folder(_, info, data):
    request = info.context["request"]
    user = load_user(info)
    if not user.is_authenticated:
        raise Exception("You can't do that!")

    logging.debug(f"Create Folder {data}")
    logging.debug(f"User {user.email}")

    site = data.get("site", None)
    path = data.get("path", None)
    parent = data.get("parent", None)

    if not site:
        logging.debug("Site is missing")
        raise Exception("Site missing!")
    if not path:
        logging.debug("Path is missing")
        raise Exception("Path missing!")

    try:
        site = Site.objects.get(id=site, user=user)
    except Site.DoesNotExist:
        raise Exception("Site not found")

    if parent:
        try:
            parent = Folder.objects.get(id=parent, site__user=user)
        except Folder.DoesNotExist:
            raise Exception("Parent folder not found")

    new_folder = Folder.objects.create(site=site, path=path, parent=parent)

    return new_folder


def resolve_update_folder(_, info, folder_id, data):
    request = info.context["request"]
    user = load_user(info)
    if not user.is_authenticated:
        raise Exception("You can't do that!")

    logging.debug(f"Update Folder {folder_id} User: {user.email} Payload: {data}")

    try:
        folder = Folder.objects.get(id=folder_id, site__user=user)
    except Folder.DoesNotExist:
        raise Exception("Folder not found")

    site = data.get("site", None)
    path = data.get("path", None)
    parent = data.get("parent", None)

    if site:
        try:
            site_obj = Site.objects.get(id=site, user=user)
            folder.site = site_obj
        except Site.DoesNotExist:
            raise Exception("Site not found")

    if parent:
        try:
            parent_obj = Folder.objects.get(id=parent, site__user=user)
            folder.parent = parent_obj
        except Folder.DoesNotExist:
            raise Exception("Parent folder not found")

    if path:
        folder.path = path

    folder.save()
    return folder
