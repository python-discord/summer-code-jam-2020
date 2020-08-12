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

class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'creator',
    ]



admin.site.register(Account, AccountAdmin)
admin.site.register(Group, GroupAdmin)
