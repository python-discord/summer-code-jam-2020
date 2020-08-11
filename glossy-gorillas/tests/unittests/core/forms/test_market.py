import pytest
from core.forms import ListInventoryRecord
from core.factories import InventoryRecordFactory


@pytest.mark.django_db
def test_no_selected_barter_method_raises_error():
    item = InventoryRecordFactory()
    form = ListInventoryRecord(item_id=item.id, data={})
    assert not form.is_valid()
    assert form.non_field_errors() == ["Specify at least one barter method"]


@pytest.mark.django_db
def test_barter_product_with_no_quantity_is_invalid():
    item = InventoryRecordFactory()
    data = {"barter_product": item.product.id}
    form = ListInventoryRecord(item_id=item.id, data=data)
    assert not form.is_valid()
    assert form.errors == {
        "barter_product_quantity": ["Specify a quantity of products you want"]
    }


@pytest.mark.parametrize(
    "data,", [{"silver_price": 30}, {"allow_offers": True}, ],
)
@pytest.mark.django_db
def test_can_list_item_with_silver_price_or_custom_offer(data):
    item = InventoryRecordFactory()
    form = ListInventoryRecord(item_id=item.id, data=data)
    assert form.is_valid()


@pytest.mark.django_db
def test_can_list_item_with_barter_product():
    item = InventoryRecordFactory()
    data = {"barter_product": item.product.id, "barter_product_quantity": 1}
    form = ListInventoryRecord(item_id=item.id, data=data)
    assert form.is_valid()
