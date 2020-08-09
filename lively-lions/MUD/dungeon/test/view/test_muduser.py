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

    def test_create_two_muduser(self):
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"

        insert_data = {'username': 'hello_world02', 'password': 'hello_world02', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 2, "Should be equal"
        assert MudUser.objects.get(pk=2).username == 'hello_world02', "Should be equal"

    def test_create_user_and_get_authenticate_and_login(self):
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"

    def test_create_user_and_login_and_login_Check_test(self):
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"

        insert_data = {'view_name': 'login_check'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Logged in', "Should be same"

    def test_create_user_and_login_and_login_Check_test_with_new_client(self):
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"

        client = Client()
        insert_data = {'view_name': 'login_check'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'invalid', "Should be same"

    def test_create_user_and_login_and_logout(self):
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"

        insert_data = {'view_name': 'login_check'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Logged in', "Should be same"
        # logout
        insert_data = {'view_name': 'logout_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Logout success', "Should be same"
        # fail login check
        insert_data = {'view_name': 'login_check'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'invalid', "Should be same"

    def test_create_user_and_login_and_logout_and_reset_now_connected_character_name(self):
        client = Client()
        # create user
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        # login user
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # login check
        insert_data = {'view_name': 'login_check'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Logged in', "Should be same"
        # logout
        insert_data = {'view_name': 'logout_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Logout success', "Should be same"
        # fail login check
        insert_data = {'view_name': 'login_check'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'invalid', "Should be same"

    def test_create_user_and_login_and_get_username(self):
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"

        insert_data = {'view_name': 'get_username'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'hello_world01', "Should be same"
