import pytest
from django.test import Client
# Create your tests here.


@pytest.fixture
def client():
    return Client()


def test_with_client(client):
    response = client.get('')
    assert response.status_code == 200
