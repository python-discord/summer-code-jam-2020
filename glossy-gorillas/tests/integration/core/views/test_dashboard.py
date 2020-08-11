import pytest
from django.shortcuts import reverse
from core.factories import TraderFactory, InventoryRecordFactory, ListingFactory


@pytest.mark.django_db
def test_user_dashboard_view_with_logged_in_user_is_ok(client):
    trader = TraderFactory()
    trader.user.set_password("password")
    trader.user.save()
    client.login(username=trader.user.username, password="password")
    response = client.get(reverse("dashboard"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_dashboard_view_with_no_user_redirects_to_login(client):
    response = client.get(reverse("dashboard"))
    assert response.status_code == 302
    assert response.url == "/login/?next=/dashboard/"


@pytest.mark.django_db
def test_user_dashboard_displays_relevant_content(client):
    """The view should display:

    1. Listings for the logged in user
    2. The user inventory
    3. The user name
    4. The user description
    """
    trader = TraderFactory()
    trader.user.set_password("password")
    trader.user.save()
    client.login(username=trader.user.username, password="password")
    inventory_item = InventoryRecordFactory(owner=trader)
    listing = ListingFactory(item__owner=trader)
    response = client.get(reverse("dashboard"))
    content = str(response.content)
    assert listing.item.product.name in content
    assert inventory_item.product.name in content
    assert trader.user.username in content
    assert trader.description in content
