import itertools
import random
from core.models.trader import Trader, InventoryRecord
from core.models.product import Product
from core.models.market import Listing, Trade, ListingStatus
from core.models.review import Review
from core.factories import trader, market, product, review
from typing import List, Tuple


def create_product_set() -> None:
    product.ProductFactory.create_batch(200)


def create_trader_set() -> None:
    trader.TraderFactory.create_batch(100)


def create_trader_inventories() -> None:
    """Create inventory objects for 75% of traders"""
    pk_list: List[int] = list(Trader.objects.values_list("id", flat=True))
    subset_count = int((len(pk_list) / 4) * 3)
    random.shuffle(pk_list)
    pk_subset = pk_list[:subset_count]
    product_pks: List[int] = list(Product.objects.values_list("id", flat=True))

    def inventory_pair(trader_pk: int) -> List[Tuple[int, int]]:
        random.shuffle(product_pks)
        return [
            (trader_pk, product_pk)
            for product_pk in product_pks[: random.randint(3, 100)]
        ]

    user_invetories = itertools.chain.from_iterable(
        [inventory_pair(pk) for pk in pk_subset]
    )

    objects = [
        trader.InventoryRecordFactory.build(owner_id=t, product_id=p)
        for t, p in user_invetories
    ]
    InventoryRecord.objects.bulk_create(objects, ignore_conflicts=True)


def create_listing_set() -> None:
    """Create listings for 60% of existing inventory records"""
    record_pks: List[int] = list(InventoryRecord.objects.values_list("id", flat=True))
    random.shuffle(record_pks)
    subset_count = int((len(record_pks) / 5) * 3)
    listings = [
        market.ListingFactory.build(item_id=x) for x in record_pks[:subset_count]
    ]

    Listing.objects.bulk_create(listings, ignore_conflicts=True)


def create_trade_set() -> None:
    """Create trade logs for 30% of existing listings"""
    listing_pks: List[int] = list(Listing.objects.values_list("id", flat=True))
    random.shuffle(listing_pks)
    subset_count = int((len(listing_pks) / 10) * 3)
    trader_pks: List[int] = Trader.objects.values_list("id", flat=True)
    trades = [
        market.TradeFactory.build(listing_id=pk, buyer_id=random.choice(trader_pks))
        for pk in listing_pks[:subset_count]
    ]

    Trade.objects.bulk_create(trades, ignore_conflicts=True)


def create_review_set() -> None:
    """Create reviews for all finalized trades"""
    trades: List[Tuple[int, int]] = list(
        Trade.objects.filter(listing__status=ListingStatus.FINALIZED.value).values_list(
            "id", "buyer__user_id"
        )
    )
    reviews = [
        review.ReviewFactory.build(user_id=buyer_id, trade_id=trade_id)
        for trade_id, buyer_id in trades
    ]
    Review.objects.bulk_create(reviews, ignore_conflicts=True)
