from django.contrib import admin
from .models import Item_Category, Small_Item, Large_Item

# Register your models here.

# Will allow us to see the admin weapon database
admin.site.register(Item_Category)
admin.site.register(Small_Item)
admin.site.register(Large_Item)
