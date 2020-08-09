from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "users"

    def ready(self):
        import users.signals
        print(users.signals.__name__)
