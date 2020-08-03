from django.contrib import admin
from .models import SongData, SongFile

# Register your models here.
class FeedFileInline(admin.TabularInline):
    model = SongFile

class FeedAdmin(admin.ModelAdmin):
    inlines = [FeedFileInline]

admin.site.register(SongData, FeedAdmin)
