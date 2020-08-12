from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver


def ignore_admin(func):
    """Admins create with manage.py createsuper user do not have a profile."""
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ObjectDoesNotExist:
            pass
    return wrapper


@receiver(user_logged_in)
@ignore_admin
def got_online(sender, user, request, **kwargs):
    user.profile.is_online = True
    user.profile.save()


@receiver(user_logged_out)
@ignore_admin
def got_offline(sender, user, request, **kwargs):
    user.profile.is_online = False
    user.profile.save()
