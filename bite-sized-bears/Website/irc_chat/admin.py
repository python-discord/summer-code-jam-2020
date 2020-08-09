from django.contrib import admin

from .models import Message, UserProfile

admin.site.register(Message)
admin.site.register(UserProfile)
