import pytest
from core import fixtures
from core import models
from core import factories


@pytest.mark.django_db
def test_product_set():
    assert models.Product.objects.count() == 0
    fixtures.create_product_set()
    assert not models.Product.objects.count() == 0


@pytest.mark.django_db
def test_trader_set():
    assert models.Trader.objects.count() == 0
    fixtures.create_trader_set()
    assert not models.Trader.objects.count() == 0


@pytest.mark.django_db
def test_trader_inventories_created_for_3_4ths_of_traders():
    factories.TraderFactory.create_batch(4)
    factories.ProductFactory.create_batch(30)
    assert models.InventoryRecord.objects.count() == 0
    fixtures.create_trader_inventories()
    assert not models.InventoryRecord.objects.count() == 0
    record_owners = models.InventoryRecord.objects.values_list(
        "owner_id", flat=True
    ).distinct()
    assert record_owners.count() == 3


@pytest.mark.django_db
def test_listings_created_for_3_5ths_of_existing_records():
    factories.InventoryRecordFactory.create_batch(5)
    assert models.Listing.objects.count() == 0
    fixtures.create_listing_set()
    assert not models.Listing.objects.count() == 0
    listed_records = models.Listing.objects.values_list("item_id", flat=True).distinct()
    assert listed_records.count() == 3


@pytest.mark.django_db
def test_trades_created_for_3_10ths_of_listings():
    factories.ListingFactory.create_batch(10)
    assert models.Trade.objects.count() == 0
    fixtures.create_trade_set()
    assert not models.Trade.objects.count() == 0
    traded_listings = models.Trade.objects.values_list(
        "listing_id", flat=True
    ).distinct()
    assert traded_listings.count() == 3
