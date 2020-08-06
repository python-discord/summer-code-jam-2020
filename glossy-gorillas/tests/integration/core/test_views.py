import pytest
from django.shortcuts import reverse
from core.factories import TraderFactory, InventoryRecordFactory, ListingFactory


def test_get_home_view_is_ok(client):
    response = client.get(reverse("home"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_listing_list_view_is_ok(client):
    response = client.get(reverse("listings"))
    assert response.status_code == 200


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


@pytest.mark.django_db
def test_login_redirects_to_user_dashboard(client):
    trader = TraderFactory()
    trader.user.set_password("password")
    trader.user.save()
    data = {"username": trader.user.username, "password": "password"}
    response = client.post(reverse("login"), data=data)
    assert response.status_code == 302
    assert response.url == reverse("dashboard")


@pytest.mark.django_db
def test_logout_redirects_to_home(client):
    trader = TraderFactory()
    trader.user.set_password("password")
    trader.user.save()
    client.login(username=trader.user.username, password="password")
    response = client.post(reverse("logout"))
    assert response.status_code == 302
    assert response.url == reverse("home")


@pytest.mark.django_db
def test_listing_search_filters_queryset_results(client):
    listing_1 = ListingFactory(item__product__name="Find Me")
    listing_2 = ListingFactory(item__product__name="Not Found")
    url = f"{reverse('listings')}?search=find"
    response = client.get(url)
    content = str(response.content)
    assert listing_1.item.product.name in content
    assert listing_2.item.product.name not in content
