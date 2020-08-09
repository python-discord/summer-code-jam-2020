from django.contrib import admin

from .models import ArticleComment, CustomUser, BlogArticle

admin.site.register(CustomUser)
admin.site.register(BlogArticle)
admin.site.register(ArticleComment)
