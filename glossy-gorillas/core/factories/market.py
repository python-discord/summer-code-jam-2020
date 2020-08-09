import factory
import random
from core.models.market import Listing, Trade, ListingStatus as LS
from core.factories.product import ProductFactory
from core.factories.trader import InventoryRecordFactory, TraderFactory


class ListingFactory(factory.DjangoModelFactory):
    item = factory.SubFactory(InventoryRecordFactory)
    silver_price = factory.LazyFunction(
        lambda: random.choice([random.randint(1, 100), None])
    )
    barter_product = factory.LazyFunction(
        lambda: random.choice([None, ProductFactory()])
    )
    barter_product_quantity = factory.LazyAttribute(
        lambda obj: random.randint(1, 100) if obj.barter_product else None
    )
    allow_offers = factory.LazyFunction(lambda: random.choice([True, False]))
    status = factory.Iterator(
        [
            LS.AVAILABLE.value,
            LS.NEGOTIATING.value,
            LS.SCHEDULED.value,
            LS.FINALIZED.value,
        ]
    )

    class Meta:
        model = Listing


class TradeFactory(factory.DjangoModelFactory):
    listing = factory.SubFactory(ListingFactory)
    buyer = factory.SubFactory(TraderFactory)

    class Meta:
        model = Trade
