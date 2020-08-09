from django.db import models
from django.utils.translation import gettext as _
from core.querysets.product import ProductQuerySet


class ProductType(models.TextChoices):
    SERVICE = "service", _("Service")
    SPICE = "spice", _("Spice")
    OBJECT = "object", _("Object")


class Product(models.Model):
    """A commodity or service that can be traded"""

    name = models.CharField(verbose_name=_("Product Name"), max_length=255)
    product_type = models.CharField(
        verbose_name=_("Product Type"),
        max_length=10,
        choices=ProductType.choices,
        default=ProductType.SPICE,
    )

    objects = ProductQuerySet.as_manager()
