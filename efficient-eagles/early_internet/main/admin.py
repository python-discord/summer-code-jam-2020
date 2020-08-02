from django.contrib import admin

from main.models import CustomUser
from main.models import Post

admin.site.register(CustomUser)
admin.site.register(Post)
