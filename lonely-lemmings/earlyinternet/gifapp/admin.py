from django.contrib import admin

from gifapp.models import Project, Image, Comment

# Register your models here.

admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Comment)
