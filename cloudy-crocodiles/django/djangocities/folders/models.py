from django.db import models

from djangocities.sites.models import Site


class Folder(models.Model):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    filename = models.CharField(max_length=256)
    path = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.site}{self.path}"


class Item(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    filename = models.CharField(max_length=256)

    class Meta:
        unique_together = ("folder", "filename")
        abstract = True
