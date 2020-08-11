from django.core.management.base import BaseCommand, CommandError
from spydir.generate_page import generate_page, authorize_page


class Command(BaseCommand):
    help = "Generates a page based on a provided page name"

    def add_arguments(self, parser):
        parser.add_argument("pages", nargs="+", type=str)

    def handle(self, *args, **options):
        for page_name in options["pages"]:

            if "," in page_name:
                args_split = page_name.split(",")
                page_name = args_split[0]
                page_type = args_split[1]
            else:
                page_type = None

            try:
                authorize_page(page_name)
                generate_page(page_name, page_type=page_type)
            except Exception as e:
                raise CommandError('Page "%s" could not be made, Error:' % page_name, e)

            self.stdout.write(self.style.SUCCESS('Successfully created page "%s"' % page_name))
