from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class NewsFeed(models.Model):
    """A news feed model to be displayed on the dashboard"""

    title = models.CharField(verbose_name=_("Title"), max_length=36)
    location = models.CharField(verbose_name=_("Location"), max_length=10)
    datetime = models.DateTimeField(
        default=timezone.now, verbose_name=_("Date Published")
    )
    description = models.TextField(verbose_name=_("Description"), max_length=225)

    def __str__(self):
        return self.title
