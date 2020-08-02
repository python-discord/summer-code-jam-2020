from django.db import models

from djangocities.cities.models import City
from djangocities.user.models import CustomUser as User

class Site(models.Model):
    class Meta:
        verbose_name_plural = "sites"
        unique_together = ('city', 'address')

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.city}/{self.address}"

class Page(models.Model):
    class Meta:
        verbose_name_plural = "pages"
        unique_together = ('site', 'filename')

    # Site
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    # Filename
    filename = models.CharField(max_length=256)
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
