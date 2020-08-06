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
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.city}/{self.address}"