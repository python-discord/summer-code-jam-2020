from django.contrib import admin
from fbbackend.models import Account
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'hashed_pass',
        'identification',
        'nickname',
        'bot'
    ]


admin.site.register(Account, AccountAdmin)
