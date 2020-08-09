# from django.contrib.auth.models import User
# from django.test import TestCase
from django.test import Client
# from django.urls import reverse
import pytest
# from mixer.backend.django import mixer
from items.test.models.test_items import CreateItem


@pytest.mark.django_db
class ItemGetTest(CreateItem):
    def test_create_method_test(self):
        client = Client()
        # item
        response = client.get('http://127.0.0.1:8000/items/category/1/')
        assert response.status_code == 200, "Should be same"
# assert response.content == b"Working POST is_working", "Should be same"
