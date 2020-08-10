import sys
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "dump fixtures"

    def handle(self, *args, **options):
        sysout = sys.stdout
        sys.stdout = open("djangocities/fixtures/initial_data.json", "w")
        call_command("dumpdata", "user", "cities", "sites", "pages")
        sys.stdout = sysout
