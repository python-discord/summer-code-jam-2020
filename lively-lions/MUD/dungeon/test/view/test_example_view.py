# from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
# from django.urls import reverse
import pytest
# from mixer.backend.django import mixer


@pytest.mark.django_db
class BaseTestCase(TestCase):
    def test_get(self):
        client = Client()
        response = client.get('http://localhost:8000/api/example/')
        assert response.content == b'Working GET', "Should be same"
        assert response.status_code == 200, "Should be same"

    def test_get_with_path(self):
        client = Client()
        response = client.get('http://localhost:8000/api/example/abc')
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Working GET', "Should be same"

    def test_get_with_404_path(self):
        client = Client()
        response = client.get('http://localhost:8000/api/example/!@#$%^&*()~_+=')
        assert response.status_code == 404, "Should be same"

    def test_post_path(self):
        client = Client()
        response = client.post('http://localhost:8000/api/example/', {'num': 'is_data'})
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Working POST is_data', "Should be same"

    # django not support PUT, DELETE
    # (https://thihara.github.io/Django-Req-Parsing/)
    # def test_put_path(self):
    #     client = Client()
    #     response = client.put('http://localhost:8000/api/example/',{'num':'is_data'})
    #     assert response.status_code == 200, "Should be same"
    #     assert response.content == b'Working PUT is_data', "Should be same"
