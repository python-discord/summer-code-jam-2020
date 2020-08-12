from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


def level_check(instance, unlock=0):
    return instance.level >= unlock


class LevelRestrictionMixin(UserPassesTestMixin):
    def handle_no_permission(self):
        return redirect("dashboard-index")
