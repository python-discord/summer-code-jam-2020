from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class Trader(models.Model):
    """Anonymous user with access to trade platform"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_("User Description"))
