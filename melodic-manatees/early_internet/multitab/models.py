from django.db import models
from django.contrib.auth.models import User


class MultiTab(models.Model):
    multitab_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=200,
        default=''
    )
    tab_one = models.CharField(
        max_length=200,
        default=''
    )
    tab_two = models.CharField(
        max_length=200,
        default=''
    )
    tab_three = models.CharField(
        max_length=200,
        default=''
    )
