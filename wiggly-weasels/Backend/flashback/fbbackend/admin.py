from django.contrib import admin
from fbbackend.models import Account, Group
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'hashed_pass',
        'nickname',
        'bot'
    ]


class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'writer',
        'content'
    ]


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'creator',
    ]



admin.site.register(Account, AccountAdmin)
admin.site.register(Group, GroupAdmin)
