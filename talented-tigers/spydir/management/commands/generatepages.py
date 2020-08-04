from django.core.management.base import BaseCommand, CommandError
from spydir.generate_page import generate_page, authorize_page

class Command(BaseCommand):
    help = 'Generates a page based on a provided page name'

    def add_arguments(self, parser):
        parser.add_argument('pages', nargs='+', type=str)

    def handle(self, *args, **options):
        for page_name in options['pages']:
            try:
                authorize_page(page_name)
                generate_page(page_name)
            except Exception as e:
                raise CommandError('Page "%s" could not be made, Error:' % page_name, e)

            self.stdout.write(self.style.SUCCESS('Successfully created page "%s"' % page_name))