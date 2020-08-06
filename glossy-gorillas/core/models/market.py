from django.db import models
from django.utils.translation import gettext as _

from core.models.product import Product
from core.models.trader import InventoryRecord, Trader


class ListingStatus(models.TextChoices):
    AVAILABLE = "A", _("Listing Available")
    NEGOTIATING = "N", _("In Negotiations")
    SCHEDULED = "S", _("Agreed and Scheduled")
    FINALIZED = "F", _("Trade Finalized")


class Listing(models.Model):
    """A listing of a possesed good on the market

    A listed item can be traded in multiple ways:
        - for a price in silver
        - for a specified quantity of another product
        - for an unspecified product

    To determine what trades are valid for a listing,
    a check is done on the corresponding fields.
    """

    item = models.ForeignKey(
        InventoryRecord, verbose_name=_("Listed Item"), on_delete=models.CASCADE
    )
    # Silver field
    silver_per_unit = models.IntegerField(
        verbose_name=_("Weight in Silver per traded unit"), null=True
    )

    # Barter Fields
    barter_product = models.ForeignKey(
        Product,
        verbose_name=_("Type of product requested for barter"),
        null=True,
        on_delete=models.CASCADE,
    )
    barter_qty_per_unit = models.IntegerField(
        verbose_name=_("Barter unit(s) per traded unit"), null=True
    )

    # Offer field
    allow_offers = models.BooleanField(
        verbose_name=_("Allow user barter offers"), default=False
    )
    status = models.CharField(
        verbose_name=_("Trade Status"),
        max_length=3,
        choices=ListingStatus.choices,
        default=ListingStatus.AVAILABLE,
    )

    def __str__(self) -> str:
        return f"{self.item.product.name}: {self.silver_per_unit} | {self.status}"


class Trade(models.Model):
    """A record of a trade between 2 users"""

    listing = models.ForeignKey(
        Listing, verbose_name=_("Trade Listing"), on_delete=models.CASCADE
    )
    buyer = models.ForeignKey(Trader, verbose_name=_("Buyer"), on_delete=models.CASCADE)