from django.db import models
from users.models import UserProfile


class MultiTab(models.Model):
    multitab_owner = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=200,
        default=''
    )
    tab_one = models.CharField(
        max_length=200,
        default='',
        blank=True
    )
    tab_two = models.CharField(
        max_length=200,
        default='',
        blank=True

    )
    tab_three = models.CharField(
        max_length=200,
        default='',
        blank=True
    )
