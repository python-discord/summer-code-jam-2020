from django.contrib import admin

from .models import Site, Page

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass
