from django.db import models

from djangocities.user.models import CustomUser as User
from djangocities.sites.models import Site


class FolderItem(models.Model):
    parent = models.ForeignKey('self', null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    filename = models.CharField(max_length=256)

    class Meta:
        abstract = True


class Folder(FolderItem):
    home_group = models.CharField(max_length=5)
    directory = models.CharField(max_length=256)
