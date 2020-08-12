from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'socl_media.apps.users'

    def ready(self):
        import socl_media.apps.users.signals
