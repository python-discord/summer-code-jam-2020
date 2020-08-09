from django.core.management.base import BaseCommand
from core import fixtures
from core.factories.trader import TraderFactory


class Command(BaseCommand):
    help = "Create a set of example data for testing"

    def handle(self, *args, **options):
        print("initializing admin user (credentials: admin/admin)...")
        trader = TraderFactory(
            user__username="admin",
            user__email="admin@teabay.com",
            user__first_name="Jimmy",
            user__last_name="Recard",
            user__is_superuser=True,
            user__is_staff=True,
        )
        trader.user.set_password("admin")
        trader.user.save()
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
        print("initializing reviews...")
        fixtures.create_review_set()
        print("initializing news feed...")
        fixtures.create_news_set()
        print("All done!")
