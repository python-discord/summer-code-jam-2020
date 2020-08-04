from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Anonymous)
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
