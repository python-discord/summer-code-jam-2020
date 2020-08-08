import pytest
from core.models import QuantityType, InventoryRecord
from core.factories import TraderFactory, ProductFactory
from django.shortcuts import reverse


def test_cannot_access_inventory_create_if_not_logged_in(client):
    response = client.get(reverse("inventory-create"))
    assert response.status_code == 302
    assert reverse("login") in response.url


@pytest.mark.django_db
def test_user_gets_inventory_form_if_logged_in(client):
    trader = TraderFactory()
    trader.user.set_password("password")
    trader.user.save()
    client.login(username=trader.user.username, password="password")
    response = client.get(reverse("inventory-create"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_valid_post_creates_inventory_record(client):
    trader = TraderFactory()
    trader.user.set_password("password")
    trader.user.save()
    client.login(username=trader.user.username, password="password")
    product = ProductFactory()
    data = {
        "product": product.id,
        "quantity": 5,
        "quantity_type": QuantityType.COUNT.value,
    }
    assert InventoryRecord.objects.count() == 0
    response = client.post(reverse("inventory-create"), data=data)
    assert response.status_code == 302
    assert response.url == reverse("dashboard")
    assert InventoryRecord.objects.count() == 1
