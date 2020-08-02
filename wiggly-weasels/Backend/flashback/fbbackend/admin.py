from django.contrib import admin
from fbbackend.models import Account, Message, Group
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'hashed_pass',
        'identification',
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
        'creatr',
        'messages',
        'identification'
    ]


admin.site.register(Account, AccountAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Group, GroupAdmin)
