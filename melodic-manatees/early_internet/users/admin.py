from django.contrib import admin
from .models import UserProfile, UserPreferences

admin.site.register(UserProfile)
admin.site.register(UserPreferences)
