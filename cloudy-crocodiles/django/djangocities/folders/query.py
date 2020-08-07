import os
import json

from djangocities.cities.models import City
from djangocities.graphql import query
from djangocities.sites.models import Site
from djangocities.pages.models import Page
from .models import Folder


@query.field("allFolders")
def resolve_all_folders(*_):
    return Folder.objects.all()


@query.field("folder")
def resolve_site(*_, id):
    return Folder.objects.get(id=id)


"""
@query.field("folderItems")
def resolve_folder_items(*_, id):
    folder = Folder.objects.get(id=id)
    result = folder.item_set.all()
    print(result)
    return result
"""


def path_to_dict(path):
    d = {"name": os.path.basename(path)}
    if os.path.isdir(path):
        d["type"] = "directory"
        d["children"] = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        d["type"] = "file"
    return d


@query.field("folderData")
def resolve_folder_data(*_, id):
    return json.dumps(path_to_dict("/cdn/xanadu/1"))
