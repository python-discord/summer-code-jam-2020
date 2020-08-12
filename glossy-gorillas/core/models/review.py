from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models.market import Trade
from django.utils.translation import gettext as _


class Review(models.Model):
    """A review given to a particular trade by the user"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))

    trade = models.OneToOneField(
        Trade, on_delete=models.CASCADE, verbose_name=_("Trade")
    )

    rating = models.IntegerField(
        verbose_name=_("Ratings"),
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        default=1,
    )

    description = models.TextField(verbose_name=_("description"), max_length=255)
