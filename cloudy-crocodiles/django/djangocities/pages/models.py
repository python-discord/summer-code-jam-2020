from django.db import models

from djangocities.sites.models import Site


class Page(models.Model):
    HTML_1 = "H1"
    HTML_2 = "H2"
    VERSION_CHOICES = [(HTML_1, "HTML 1"), (HTML_2, "HTML 2")]

    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    version = models.CharField(max_length=2, choices=VERSION_CHOICES, default=HTML_1)
    file_name = models.CharField(max_length=256)
    content = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "pages"

    def __str__(self):
        return self.file_name
