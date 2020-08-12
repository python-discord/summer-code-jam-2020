from django.contrib import admin

from .models import Battle, Challenger


@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    pass


@admin.register(Challenger)
class ChallengerAdmin(admin.ModelAdmin):
    pass
