from django.apps import AppConfig
from django.db.models.signals import post_save


class UsersConfig(AppConfig):
    name = "users"

    def ready(self):
        from django.contrib.auth.models import User
        from users.signals import create_profile, save_profile

        post_save.connect(create_profile, sender=User)
        post_save.connect(save_profile, sender=User)
