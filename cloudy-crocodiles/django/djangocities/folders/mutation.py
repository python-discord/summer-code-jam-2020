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

    site = data["site"]
    path = data["path"]
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
