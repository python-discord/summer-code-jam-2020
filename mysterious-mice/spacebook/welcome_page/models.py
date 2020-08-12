from django.db import models


class VisitCount(models.Model):
    num_visits = models.IntegerField(default=0)
