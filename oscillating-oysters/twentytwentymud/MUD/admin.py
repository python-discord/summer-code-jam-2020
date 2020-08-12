from django.contrib import admin

from .models import Room, Player, Server

admin.site.register(Room)
admin.site.register(Player)
admin.site.register(Server)

# Register your models here.
