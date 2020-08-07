from django.contrib import admin

from .models import CustomUser, BlogArticle

admin.site.register(CustomUser)
admin.site.register(BlogArticle)
