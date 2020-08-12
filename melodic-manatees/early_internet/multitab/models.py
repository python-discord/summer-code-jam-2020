from django.db import models
from users.models import UserProfile


class MultiTab(models.Model):
    '''Model for Multitabs, takes one title field and three URL's
    URL's must be complete (example: https://www.google.com/)'''
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
