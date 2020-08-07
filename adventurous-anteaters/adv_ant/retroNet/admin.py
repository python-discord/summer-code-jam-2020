from django.contrib import admin
from .models import Tweet


class TweetAdmin(admin.ModelAdmin):
    list_display = ('content',)


admin.site.register(Tweet,TweetAdmin)
