from django.db import models
from django.conf import settings

from djangocities.folders.models import FolderItem


class Page(FolderItem):
    class Meta:
        verbose_name_plural = "pages"
        unique_together = ('site', 'filename')

    # Version
    HTML_1 = 'H1'
    HTML_2 = 'H2'
    VERSION_CHOICES = [
        ('H1', 'HTML 1'),
        ('H2', 'HTML 2')
    ]
    version = models.CharField(
        max_length=2,
        choices=VERSION_CHOICES,
        default=HTML_1
    )
    # Content
    content = models.TextField(blank=True)

    def __str__(self):
        return self.filename

    def save(self, *args, **kwargs):
        super(Page, self).save(*args, **kwargs)
        filepath = f"{settings.MEDIA_ROOT}/{self.folder}/{self.filename}"
        fout = open(filepath, 'w')
        fout.write(self.content)
