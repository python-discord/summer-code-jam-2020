# from django.test import TestCase
# from django.contrib.auth.models import User
import pytest
from .test_base import BaseTestCase
from dungeon.models.character import MudUser, Character
# from mixer.backend.django import mixer


@pytest.mark.django_db
class CharacterBaseTestCase(BaseTestCase):
    def test_create_user_and_create_character(self):
        user = MudUser.objects.create(username='Hello_World')
        Character.objects.create(user=user, name="c_Hello_World")
        assert Character.objects.get(pk=1).name == "c_Hello_World", "Should be equal"
        assert Character.objects.count() == 1, "Should be equal"

    def test_create_user_and_create_character_check_stats(self):
        user = MudUser.objects.create(username='Hello_World')
        Character.objects.create(user=user, name="c_Hello_World")
        assert Character.objects.count() == 1, "Should be equal"
        assert Character.objects.get(pk=1).name == "c_Hello_World", "Should be equal"
        assert Character.objects.get(pk=1).hp == 100, "Should be equal"
        assert Character.objects.get(pk=1).total_attack == 11, "Should be equal"
        assert Character.objects.get(pk=1).total_defense == 11, "Should be equal"
        assert Character.objects.get(user=user).user == user, "Should be equal"

    def test_create_user_and_create_character_check_stats_with_filter(self):
        user = MudUser.objects.create(username='Hello_World')
        Character.objects.create(user=user, name="c_Hello_World")
        assert Character.objects.count() == 1, "Should be equal"
        assert Character.objects.get(pk=1).name == "c_Hello_World", "Should be equal"
        assert Character.objects.get(pk=1).hp == 100, "Should be equal"
        assert Character.objects.get(pk=1).total_attack == 11, "Should be equal"
        assert Character.objects.get(pk=1).total_defense == 11, "Should be equal"
        assert Character.objects.filter(user=user).count() == 1, "Should be equal"
        assert Character.objects.filter(user=user)[0].user == user, "Should be equal"

    def test_create_user_and_create_two_character_filter_character(self):
        user = MudUser.objects.create(username='Hello_World')
        Character.objects.create(user=user, name="first_Hello_World")
        Character.objects.create(user=user, name="second_Hello_World")
        assert Character.objects.count() == 2, "Should be equal"
        assert Character.objects.get(pk=1).name == "first_Hello_World", "Should be equal"
        assert Character.objects.get(pk=1).hp == 100, "Should be equal"
        assert Character.objects.get(pk=1).total_attack == 11, "Should be equal"
        assert Character.objects.get(pk=1).total_defense == 11, "Should be equal"
        assert Character.objects.filter(user=user)[0].user == user, "Should be equal"
        assert Character.objects.filter(user=user)[0].name == 'first_Hello_World', "Should be equal"
        assert Character.objects.filter(user=user)[1].user == user, "Should be equal"
        assert Character.objects.filter(user=user)[1].name == 'second_Hello_World', "Should be equal"
