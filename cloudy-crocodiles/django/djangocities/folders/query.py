import os
from pathlib import Path

from djangocities.cities.models import City
from djangocities.graphql import query
from djangocities.sites.models import Site
from djangocities.pages.models import Page
from djangocities.user_media.models import Image

from .models import Folder


@query.field("allFolders")
def resolve_all_folders(*_):
    return Folder.objects.all()


@query.field("folder")
def resolve_site(*_, id):
    return Folder.objects.get(id=id)


models = {".html": Page, ".gif": Image}

"""
def path_to_dict(folder, path):
    filename = os.path.basename(path)
    d = {"__typename": "Item", "filename": filename}
    if os.path.isdir(path):
        obj = Folder.objects.get(path=path)
        d["collection"] = "folders"
        d["children"] = [path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        obj = Page.objects.get(folder=folder, filename=filename)
        d["collection"] = "pages"
    d["id"] = obj.id
    return d
"""


def path_to_items(folder, path):
    items = []
    for filename in os.listdir(path):
        d = {"__typename": "Item", "filename": filename}
        itemPath = os.path.join(path, filename)
        if os.path.isdir(itemPath):
            obj = Folder.objects.get(parent=folder, filename=filename)
            d["collection"] = "folders"
        else:
            ext = Path(filename).suffix
            model = models[ext]
            obj = model.objects.get(folder=folder, filename=filename)
            # d["collection"] = "pages"
            d["collection"] = model._meta.verbose_name_plural
        d["id"] = obj.id
        items.append(d)
    return items


@query.field("folderItems")
def resolve_folder_items(*_, id):
    folder = Folder.objects.get(id=id)
    # d = path_to_dict(folder, os.path.join("/cdn", str(folder)))
    # return d["children"]
    return path_to_items(folder, os.path.join("/cdn", str(folder)))


"""
@query.field("folderData")
def resolve_folder_data(*_, id):
    return json.dumps(path_to_dict("/cdn/xanadu/1"))
"""

"""
@query.field("folderItems")
def resolve_folder_items(*_, id):
    folder = Folder.objects.get(id=id)
    result = folder.item_set.all()
    print(result)
    return result
"""
