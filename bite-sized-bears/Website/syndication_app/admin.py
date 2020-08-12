from django.contrib import admin

from .models import User, Community, Post, Comments

admin.site.register(User)
admin.site.register(Community)
admin.site.register(Post)
admin.site.register(Comments)
