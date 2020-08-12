from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from core.models.product import Product


class QuantityType(models.TextChoices):
    COUNT = "C", _("Count")
    WEIGHT_G = "G", _("Weight in Grams")
    WEIGHT_KG = "K", _("Weight in Kilograms")


class Trader(models.Model):
    """Anonymous user with access to trade platform"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_("User Description"))


class InventoryRecord(models.Model):
    """Record of goods possesed by trader of a given product"""

    owner = models.ForeignKey(Trader, verbose_name=_("Owner"), on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name=_("Product"), on_delete=models.PROTECT
    )
    quantity = models.IntegerField(verbose_name=_("Quantity"))
    quantity_type = models.CharField(
        verbose_name=_("Quantity Type"), choices=QuantityType.choices, max_length=3
    )
