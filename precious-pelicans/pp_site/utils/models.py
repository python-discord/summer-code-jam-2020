from django.db import models


class TimeStampMixin(models.Model):
    """A model that stores when it was created, and updated"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
