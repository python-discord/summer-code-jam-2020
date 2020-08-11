from django.contrib import admin

from .models import ForumPost, ForumPostReply

admin.site.register(ForumPost)
admin.site.register(ForumPostReply)
