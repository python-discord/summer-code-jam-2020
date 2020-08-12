from django.contrib import admin
from .models import Tweet, UpdateProfile


class TweetAdmin(admin.ModelAdmin):
    list_display = ('content',)


class UpdateProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'about')


admin.site.register(Tweet, TweetAdmin)
admin.site.register(UpdateProfile, UpdateProfileAdmin)
