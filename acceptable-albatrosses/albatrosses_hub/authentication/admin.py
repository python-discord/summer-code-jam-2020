from django.contrib import admin
from .models import HubUser


class HubUserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "password")


admin.site.register(HubUser, HubUserAdmin)
