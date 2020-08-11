import pytest
from django.shortcuts import reverse
from core.models import User, Trader


@pytest.mark.django_db
def test_register_with_valid_data_creates_user_and_trader(client):
    data = {
        "username": "veszappa",
        "first_name": "Jimmy",
        "last_name": "Recard",
        "email": "JRRecard@pydis.com",
        "password1": "eHQWZyuDNQxWR35AFRfnRv",
        "password2": "eHQWZyuDNQxWR35AFRfnRv",
    }
    assert User.objects.count() == 0
    assert Trader.objects.count() == 0
    response = client.post(reverse("register"), data=data)
    assert response.status_code == 302
    assert response.url == reverse("home")
    assert User.objects.count() == 1
    assert Trader.objects.count() == 1
