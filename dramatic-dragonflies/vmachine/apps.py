from django.apps import AppConfig


class VmachineConfig(AppConfig):
    name = 'vmachine'

    def ready(self):
        import vmachine.signals
