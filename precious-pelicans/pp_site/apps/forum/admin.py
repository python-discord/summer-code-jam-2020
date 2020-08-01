from django.contrib import admin
from .models import ForumPostOriginal, ForumPostReply


admin.site.register(ForumPostOriginal)
admin.site.register(ForumPostReply)
