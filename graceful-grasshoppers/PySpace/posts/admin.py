from django.contrib import admin
from .models import Post, Like, Dislike, PostComment

admin.site.register(Post)
admin.site.register(Dislike)
admin.site.register(Like)
admin.site.register(PostComment)
