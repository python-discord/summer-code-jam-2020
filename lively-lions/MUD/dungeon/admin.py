from django.contrib import admin
from dungeon.models.character import MudUser, Character

# Register your models here.

# Will allow us to see the admin weapon database
admin.site.register(MudUser)
admin.site.register(Character)
