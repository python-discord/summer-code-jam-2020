from django.contrib import admin
from .models import Message, UserProfile
# Register your models here.

admin.site.register(Message)
admin.site.register(UserProfile)
