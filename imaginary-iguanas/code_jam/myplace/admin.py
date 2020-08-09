from django.contrib import admin

from .models import BlogPost, BlogComment, ProfileComment


admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(ProfileComment)
