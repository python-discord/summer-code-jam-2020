from django.contrib import admin

from .models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
