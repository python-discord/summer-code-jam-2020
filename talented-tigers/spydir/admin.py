from django.contrib import admin
from .models import BlogPost, GeneratedPage, PageImage, Ingredient, Step

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(GeneratedPage)
admin.site.register(PageImage)
admin.site.register(Ingredient)
admin.site.register(Step)
