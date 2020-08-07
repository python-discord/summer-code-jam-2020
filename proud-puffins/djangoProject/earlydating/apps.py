from django.apps import AppConfig


class EarlydatingConfig(AppConfig):
    name = 'earlydating'

    def ready(self):
        pass  # import earlydating.signals
