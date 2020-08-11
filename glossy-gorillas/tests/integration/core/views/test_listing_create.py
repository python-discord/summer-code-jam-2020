import pytest
from django.shortcuts import reverse
from django.contrib.messages import get_messages
from core.models import Listing
from core.factories import InventoryRecordFactory, TraderFactory


@pytest.mark.django_db
def test_get_create_view_with_valid_item_and_looged_in_user_id_is_ok(client):
    trader = TraderFactory()
    record = InventoryRecordFactory(owner=trader)
    user = trader.user
    user.set_password("password")
    user.save()
    client.login(username=user.username, password="password")
    response = client.get(reverse("listing-create", kwargs={"item_id": record.id}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_create_view_with_not_owned_item_redirects_to_dashboard_with_message(
    client,
):
    trader = TraderFactory()
    record = InventoryRecordFactory()
    user = trader.user
    user.set_password("password")
    user.save()
    client.login(username=user.username, password="password")
    response = client.get(reverse("listing-create", kwargs={"item_id": record.id}))
    assert response.status_code == 302
    messages = messages = [
        str(message) for message in get_messages(response.wsgi_request)
    ]
    assert messages == ["The record you want to list does not exist"]


@pytest.mark.django_db
def test_valid_post_to_create_view_creates_listing(client):
    trader = TraderFactory()
    record = InventoryRecordFactory(owner=trader)
    user = trader.user
    user.set_password("password")
    user.save()
    client.login(username=user.username, password="password")
    data = {"silver_price": 30}
    assert Listing.objects.count() == 0
    response = client.post(
        reverse("listing-create", kwargs={"item_id": record.id}), data=data
    )
    assert response.status_code == 302
    messages = messages = [
        str(message) for message in get_messages(response.wsgi_request)
    ]
    assert messages == ["Listing created!"]
    assert Listing.objects.count() == 1
