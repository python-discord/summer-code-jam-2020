from django.contrib import admin

# Register your models here.
from .models import ChatRoom, ChatMessage

admin.site.register(ChatRoom)
admin.site.register(ChatMessage)
