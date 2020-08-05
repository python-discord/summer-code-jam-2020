from django.contrib import admin

from .models import Folder


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("name",)}
    pass
