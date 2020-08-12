import pytest
from core.factories import TraderFactory
from django.shortcuts import reverse


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
