from django.core.management.base import BaseCommand
from core import fixtures
from core.factories.trader import TraderFactory


class Command(BaseCommand):
    help = "Create a set of example data for testing"

    def handle(self, *args, **options):
        print("initializing admin user...")
        trader = TraderFactory(
            user__username="admin",
            user__email="admin@teabay.com",
            user__first_name="Jimmy",
            user__last_name="Recard",
        )
        trader.user.set_password("admin")
        print("initializing traders...")
        fixtures.create_trader_set()
        print("initializing products...")
        fixtures.create_product_set()
        print("initializing inventories...")
        fixtures.create_trader_inventories()
        print("initializing listings...")
        fixtures.create_listing_set()
        print("initializing trades...")
        fixtures.create_trade_set()
        print("All done!")
