# from django.contrib.auth.models import User
# from django.test import TestCase
from django.test import Client
# from django.urls import reverse
import pytest
# from mixer.backend.django import mixer
from .test_base import BaseTestCase
from dungeon.models.character import MudUser, Character


@pytest.mark.django_db
class CharacterTestCase(BaseTestCase):
    def test_base_create_user_and_login(self):
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

    def test_and_create_character(self):
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
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"

    def test_and_create_two_samename_character(self):
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
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create samename character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "invalid".encode(), "Should be same"

    def test_and_create_character_get_character_list(self):
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
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # get character
        insert_data = {'view_name': 'get_character_list'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "hello_name".encode(), "Should be same"

    def test_and_not_character_get_character_list(self):
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
        # get character
        insert_data = {'view_name': 'get_character_list'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "invalid".encode(), "Should be same"

    def test_and_create_two_character_get_character_list(self):
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
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name02'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # get character
        insert_data = {'view_name': 'get_character_list'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "hello_name01,hello_name02".encode(), "Should be same"

    def test_and_create_character_and_get_character_stats(self):
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
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # get character stats
        insert_data = {'view_name': 'get_character_stats', 'character_name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == \
            "hello_name01 hp : 100/100 total attack : 11 attack cool time : 3.0 total defense : 11".encode(), \
            "Should be same"

    def test_and_create_character_and_update_character_stats_and_get_stats(self):
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
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # update character stats # hp | max_hp | total_attack | total_defense # only UP
        # max_hp
        insert_data = \
            {'view_name': 'update_character_stats', 'stats': 'max_hp', 'num': '1', 'character_name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "Success max_hp changed".encode(), "Should be same"
        # hp
        insert_data = \
            {'view_name': 'update_character_stats', 'stats': 'hp', 'num': '1', 'character_name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "Success hp changed".encode(), "Should be same"
        # total_attack
        insert_data = \
            {'view_name': 'update_character_stats', 'stats': 'total_attack',
                'num': '2', 'character_name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "Success total attack changed".encode(), "Should be same"
        # total_defense
        insert_data = \
            {'view_name': 'update_character_stats', 'stats': 'total_defense',
                'num': '3', 'character_name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "Success total defense changed".encode(), "Should be same"
        # get character stats
        insert_data = {'view_name': 'get_character_stats', 'character_name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == \
            "hello_name01 hp : 101/101 total attack : 13 attack cool time : 3.0 total defense : 14".encode(), \
            "Should be same"
        # total_cool_time
        insert_data = \
            {'view_name': 'update_character_stats', 'stats': 'attack_cool_time',
                'num': '-0.2', 'character_name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "Success attack cool time changed".encode(), "Should be same"
        # get character stats
        insert_data = {'view_name': 'get_character_stats', 'character_name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == \
            "hello_name01 hp : 101/101 total attack : 13 attack cool time : 2.8 total defense : 14".encode(), \
            "Should be same"

    def test_and_select_character(self):
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        # log in
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name02'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # select character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # check now_connected_character_name
        user = MudUser.objects.get(pk=1)
        assert user.now_connected_character_name == insert_data['name'], "Should be same"
        # select character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name02'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # check now_connected_character_name
        user = MudUser.objects.get(pk=1)
        assert user.now_connected_character_name == insert_data['name'], "Should be same"

    def test_logout_check_now_connected_character_name(self):
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        # log in
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name02'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # select first character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # check now_connected_character_name
        user = MudUser.objects.get(pk=1)
        assert user.now_connected_character_name == insert_data['name'], "Should be same"
        # select second character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name02'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # check now_connected_character_name
        insert_data = {'view_name': 'logout_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Logout success', "Should be same"
        user = MudUser.objects.get(pk=1)
        assert user.now_connected_character_name == '', "Should be same"

    def test_select_character_and_get_user_list_in_samelocation(self):
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        # log in
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name02'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # select first character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # check now_connected_character_name
        user = MudUser.objects.get(pk=1)
        assert user.now_connected_character_name == insert_data['name'], "Should be same"
        # get user list in same room
        insert_data = {'view_name': 'get_userlist_in_room'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "hello_name01".encode(), "Should be same"

    def test_select_character_and_get_two_user_list_in_samelocation(self):
        client = Client()
        # USer 1
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        # log in
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name02'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # select first character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # check now_connected_character_name
        user = MudUser.objects.get(pk=1)
        assert user.now_connected_character_name == insert_data['name'], "Should be same"
        # get user list in same room
        insert_data = {'view_name': 'get_userlist_in_room'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "hello_name01".encode(), "Should be same"
        # USER 2
        client02 = Client()
        insert_data = {'username': 'hello_world02', 'password': 'hello_world02', 'view_name': 'create_user'}
        response = client02.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 2, "Should be equal"
        assert MudUser.objects.get(pk=2).username == 'hello_world02', "Should be equal"
        # log in
        client02 = Client()
        insert_data = {'username': 'hello_world02', 'password': 'hello_world02', 'view_name': 'login_user'}
        response = client02.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name03'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name04'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # select first character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name03'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # get user list in same room
        insert_data = {'view_name': 'get_userlist_in_room'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "hello_name01,hello_name03".encode(), "Should be same"

    def test_two_character_in_same_room_and_attack_user1_to_user2(self):
        client = Client()
        # USer 1
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        # log in
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name02'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # select first character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # check now_connected_character_name
        user = MudUser.objects.get(pk=1)
        assert user.now_connected_character_name == insert_data['name'], "Should be same"
        # get user list in same room
        insert_data = {'view_name': 'get_userlist_in_room'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "hello_name01".encode(), "Should be same"
        # USER 2
        client02 = Client()
        insert_data = {'username': 'hello_world02', 'password': 'hello_world02', 'view_name': 'create_user'}
        response = client02.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 2, "Should be equal"
        assert MudUser.objects.get(pk=2).username == 'hello_world02', "Should be equal"
        # log in
        client02 = Client()
        insert_data = {'username': 'hello_world02', 'password': 'hello_world02', 'view_name': 'login_user'}
        response = client02.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name03'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name04'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # select first character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name03'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # get user list in same room
        insert_data = {'view_name': 'get_userlist_in_room'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "hello_name01,hello_name03".encode(), "Should be same"
        # now client USER2 - attack hello_name03 -> hello_name01
        insert_data = {'view_name': 'attack_character', 'target_user': 'hello_name01'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert Character.objects.get(name='hello_name01').hp == 90, "Should be same"
        assert response.content == "Success attack hello_name01 -> hp : 90".encode(), "Should be same"

    def test_two_character_in_same_room_and_attack_user2_to_user2(self):
        client = Client()
        # USer 1
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        # log in
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name02'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # select first character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # check now_connected_character_name
        user = MudUser.objects.get(pk=1)
        assert user.now_connected_character_name == insert_data['name'], "Should be same"
        # get user list in same room
        insert_data = {'view_name': 'get_userlist_in_room'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "hello_name01".encode(), "Should be same"
        # USER 2
        client02 = Client()
        insert_data = {'username': 'hello_world02', 'password': 'hello_world02', 'view_name': 'create_user'}
        response = client02.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 2, "Should be equal"
        assert MudUser.objects.get(pk=2).username == 'hello_world02', "Should be equal"
        # log in
        client02 = Client()
        insert_data = {'username': 'hello_world02', 'password': 'hello_world02', 'view_name': 'login_user'}
        response = client02.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name03'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name04'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # select first character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name03'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # get user list in same room
        insert_data = {'view_name': 'get_userlist_in_room'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "hello_name01,hello_name03".encode(), "Should be same"
        # now client USER2 - attack hello_name03 -> hello_name03
        insert_data = {'view_name': 'attack_character', 'target_user': 'hello_name03'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert Character.objects.get(name='hello_name03').hp == 100, "Should be same"
        assert response.content == "invalid".encode(), "Should be same"
        # now client USER2 - attack hello_name03 -> hello_name03
        insert_data = {'view_name': 'attack_character', 'target_user': 'hello_name999'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert Character.objects.get(name='hello_name03').hp == 100, "Should be same"
        assert response.content == "invalid".encode(), "Should be same"

    def test_two_character_in_same_room_and_big_attack_user2_to_user1(self):
        client = Client()
        # USer 1
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'create_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == 'hello_world01', "Should be equal"
        # log in
        client = Client()
        insert_data = {'username': 'hello_world01', 'password': 'hello_world01', 'view_name': 'login_user'}
        response = client.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name02'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # select first character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name01'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # check now_connected_character_name
        user = MudUser.objects.get(pk=1)
        assert user.now_connected_character_name == insert_data['name'], "Should be same"
        # get user list in same room
        insert_data = {'view_name': 'get_userlist_in_room'}
        response = client.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "hello_name01".encode(), "Should be same"
        # USER 2
        client02 = Client()
        insert_data = {'username': 'hello_world02', 'password': 'hello_world02', 'view_name': 'create_user'}
        response = client02.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create User {insert_data['username']}".encode(), "Should be same"
        assert MudUser.objects.count() == 2, "Should be equal"
        assert MudUser.objects.get(pk=2).username == 'hello_world02', "Should be equal"
        # log in
        client02 = Client()
        insert_data = {'username': 'hello_world02', 'password': 'hello_world02', 'view_name': 'login_user'}
        response = client02.post('http://localhost:8000/api/muduser/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == b'Login success', "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name03'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # create character
        insert_data = {'view_name': 'create_character', 'name': 'hello_name04'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success create character {insert_data['name']}".encode(), "Should be same"
        # select first character
        insert_data = {'view_name': 'select_character', 'name': 'hello_name03'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == f"Success Character Select {insert_data['name']}".encode(), "Should be same"
        # get user list in same room
        insert_data = {'view_name': 'get_userlist_in_room'}
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        assert response.content == "hello_name01,hello_name03".encode(), "Should be same"
        # now client USER2 - attack hello_name03 -> hello_name01
        insert_data = {'view_name': 'attack_character', 'target_user': 'hello_name01'}
        attacker = Character.objects.get(name='hello_name03')
        attacker.total_attack = 99999
        attacker.save()
        response = client02.post('http://localhost:8000/api/character/', insert_data)
        assert response.status_code == 200, "Should be same"
        # dead reset hp
        assert Character.objects.get(name='hello_name01').hp == 100, "Should be same"
        assert Character.objects.get(name='hello_name01').location_x == 10, "Should be same"
        assert Character.objects.get(name='hello_name01').location_y == 10, "Should be same"
        assert Character.objects.get(name='hello_name01').location_z == 10, "Should be same"
        assert response.content == "Success attack hello_name01 -> Dead".encode(), "Should be same"
