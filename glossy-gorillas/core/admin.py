from django.contrib import admin
from core import models

admin.site.register(models.Review)

admin.site.register(models.Listing)
admin.site.register(models.Trade)

admin.site.register(models.Product)

admin.site.register(models.Trader)
admin.site.register(models.InventoryRecord)
