from django.contrib import admin

# Register your models here.

from .models import Profile, UserVote


admin.site.register(Profile)
admin.site.register(UserVote)
