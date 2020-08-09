from django.contrib import admin
from .models import BlogPost, GeneratedPage, PageImage

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(GeneratedPage)
admin.site.register(PageImage)
