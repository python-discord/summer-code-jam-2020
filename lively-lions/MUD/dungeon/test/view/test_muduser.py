# from django.contrib.auth.models import User
# from django.test import TestCase
from django.test import Client
# from django.urls import reverse
import pytest
# from mixer.backend.django import mixer
from .test_base import BaseTestCase
from dungeon.models.character import MudUser


@pytest.mark.django_db
class mudUserTestCase(BaseTestCase):
    def test_create_method_test(self):
        client = Client()
        insert_data = {'view_name': 'is_working'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b"Working POST is_working", "Should be same"

    def test_create_method_multiple_data_test(self):
        client = Client()
        insert_data = {'view_name': 'is_working', 'multiple_data': 'is_multiple'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b"Working multiple_data POST is_multiple", "Should be same"

    def test_create_hello_world_muduser(self):
        client = Client()
        insert_data = {'username': 'hello_world', 'password': 'hello_world', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world', "Should be equal"
