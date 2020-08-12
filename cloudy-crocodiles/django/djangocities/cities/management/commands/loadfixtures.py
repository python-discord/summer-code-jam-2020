from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "load fixtures"

    def handle(self, *args, **options):
        call_command("flush", verbosity=0, interactive=False)
        call_command("loaddata", "djangocities/fixtures/initial_data.json")
