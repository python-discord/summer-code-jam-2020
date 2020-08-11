from django.apps import AppConfig


class VmachineConfig(AppConfig):
    name = 'vmachine'

    def ready(self) -> None:
        import vmachine.signals  # NOQA: F401
