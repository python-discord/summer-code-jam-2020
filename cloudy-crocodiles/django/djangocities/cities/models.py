from django.db import models


class City(models.Model):
    class Meta:
        verbose_name_plural = "cities"

    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=500)
    slug = models.SlugField()

    def __str__(self):
        return self.slug
