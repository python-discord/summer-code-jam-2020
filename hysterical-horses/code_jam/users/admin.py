from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Account

admin.site.register(Profile)


class AccountAdmin(UserAdmin):
    list_display = ("email", "username", "date_joined", "last_login")
    search_fields = ("email", "username")
    readonly_fields = ("password", "last_login", "date_joined")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
