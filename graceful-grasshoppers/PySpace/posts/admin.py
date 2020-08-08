from django.contrib import admin
from .models import Post, Like, Dislike, PostComment

# Register your models here.
admin.site.register(Post)
admin.site.register(Dislike)
admin.site.register(Like)
admin.site.register(PostComment)
