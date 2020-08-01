from django.contrib import admin

from .models import Template, Webpage, Comment

# Register your models here.
admin.site.register(Template)
admin.site.register(Webpage)
admin.site.register(Comment)
