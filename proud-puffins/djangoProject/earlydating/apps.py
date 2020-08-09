from django.apps import AppConfig


class EarlydatingConfig(AppConfig):
    name = 'earlydating'

    def ready(self):
        # Import is necessary for signals to work despite lint errors
        import earlydating.signals
