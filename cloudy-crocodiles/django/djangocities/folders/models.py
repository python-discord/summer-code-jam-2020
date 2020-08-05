from django.db import models

from djangocities.user.models import CustomUser as User
from djangocities.sites.models import Site


class Folder(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    directory = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.site}{self.directory}"


class FolderItem(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    filename = models.CharField(max_length=256)

    class Meta:
        abstract = True
