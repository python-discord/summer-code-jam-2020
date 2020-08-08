from django.db import models
from django.core.exceptions import ValidationError

from djangocities.sites.models import Site
from djangocities.utils.validation.django.html_validator import validate_html
from djangocities.utils.validation.html.exceptions import HtmlValidationException


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

    def clean(self):
        # Validate HTML
        if self.version == self.HTML_1:
            ver = 1
        elif self.version == self.HTML_2:
            ver = 2
        else:
            raise ValidationError("Unsupported HTML version")

        try:
            validate_html(self.content, ver)
        except HtmlValidationException as e:
            raise ValidationError(e)
