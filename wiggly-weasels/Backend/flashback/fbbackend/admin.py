from django.contrib import admin
from fbbackend.models import Account, Message, Group, Post
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


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'identification',
        'creator',
        'content',
        'title',
        'comments'
    ]


admin.site.register(Account, AccountAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
