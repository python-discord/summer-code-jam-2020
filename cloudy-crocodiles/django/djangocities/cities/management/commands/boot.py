from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "boot"

    def handle(self, *args, **options):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "djangocities/fixtures/initial_data.json")
