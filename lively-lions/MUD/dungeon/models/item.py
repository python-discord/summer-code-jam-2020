# from django.contrib.auth.models import User
from django.db import models


# Temporary model for test
class Item(models.Model):
    inventory = models.ForeignKey("Inventory", on_delete=models.CASCADE)
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
