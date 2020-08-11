# from django.contrib.auth.models import User
# from django.test import TestCase
import json
from django.test import Client
from django.forms.models import model_to_dict
# from django.urls import reverse
import pytest
# from mixer.backend.django import mixer
from items.test.models.test_items import CreateItem


@pytest.mark.django_db
class SmallItemGetTest(CreateItem):
    def test_get_small_item(self):
        client = Client()
        item_id = 1
        obj = self.small_buckler
        dict_obj = model_to_dict(obj)
        serial = json.dumps(dict_obj)
        response = client.get(f'http://127.0.0.1:8000/items/small_item/{item_id}/')
        assert response.status_code == 200, "Should be same"
        assert response.content == f'{serial}'.encode(), "Should be same"
