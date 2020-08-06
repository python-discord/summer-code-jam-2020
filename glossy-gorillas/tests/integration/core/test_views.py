import pytest
from django.shortcuts import reverse
from core.factories import TraderFactory


def test_get_home_view_is_ok(client):
    response = client.get(reverse("home"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_listing_list_view_is_ok(client):
    response = client.get(reverse("listings"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_dashboard_view_is_ok(client):
    trader = TraderFactory()
    response = client.get(reverse("dashboard", kwargs={"pk": trader.id}))
    assert response.status_code == 200