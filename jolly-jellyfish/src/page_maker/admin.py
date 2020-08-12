from django.contrib import admin

from .models import Template, Webpage, Comment, Like

# Register your models here.
admin.site.register(Template)
admin.site.register(Webpage)
admin.site.register(Comment)
admin.site.register(Like)
