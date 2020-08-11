# from django.test import TestCase
from django.contrib.auth.models import User
import pytest
from .test_base import BaseTestCase
from dungeon.models.character import MudUser


@pytest.mark.django_db
class UseBaseTestCase(BaseTestCase):

    def test_make_hello_world_muduser(self):
        hello = BaseTestCase()
        user = hello.create_hello_world_muduser()
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == user.username, "Should be equal"

    def test_make_one_muduser_with_mixer(self):
        one = BaseTestCase()
        user = one.create_one_muduser()
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == user.username, "Should be equal"

    def test_make_two_muduser_with_mixer(self):
        two = BaseTestCase()
        user1 = two.create_one_muduser()
        user2 = two.create_one_muduser()
        assert MudUser.objects.count() == 2, "Should be equal"
        assert MudUser.objects.get(pk=1).username == user1.username, "Should be equal"
        assert MudUser.objects.get(pk=2).username == user2.username, "Should be equal"

    def test_make_three_muduser_with_mixer(self):
        three = BaseTestCase()
        user1, user2, user3 = three.create_three_muduser()

        assert MudUser.objects.count() == 3, "Should be equal"
        assert MudUser.objects.get(pk=1).username == user1.username, "Should be equal"
        assert MudUser.objects.get(pk=2).username == user2.username, "Should be equal"
        assert MudUser.objects.get(pk=3).username == user3.username, "Should be equal"

    def test_make_many_muduser_with_mixer(self):
        many = BaseTestCase()
        many.create_many_muduser()
        assert MudUser.objects.count() == 50, "Should be equal"

    def test_make_hello_world_user(self):
        hello = BaseTestCase()
        user = hello.create_hello_world_user()
        assert User.objects.count() == 1, "Should be equal"
        assert User.objects.get(pk=1).username == user.username, "Should be equal"

    def test_make_one_user_with_mixer(self):
        one = BaseTestCase()
        user = one.create_one_user()
        assert User.objects.count() == 1, "Should be equal"
        assert User.objects.get(pk=1).username == user.username, "Should be equal"

    def test_make_two_user_with_mixer(self):
        two = BaseTestCase()
        user1 = two.create_one_user()
        user2 = two.create_one_user()
        assert User.objects.count() == 2, "Should be equal"
        assert User.objects.get(pk=1).username == user1.username, "Should be equal"
        assert User.objects.get(pk=2).username == user2.username, "Should be equal"

    def test_make_three_user_with_mixer(self):
        three = BaseTestCase()
        user1, user2, user3 = three.create_three_user()

        assert User.objects.count() == 3, "Should be equal"
        assert User.objects.get(pk=1).username == user1.username, "Should be equal"
        assert User.objects.get(pk=2).username == user2.username, "Should be equal"
        assert User.objects.get(pk=3).username == user3.username, "Should be equal"

    def test_make_many_user_with_mixer(self):
        many = BaseTestCase()
        many.create_many_user()
        assert User.objects.count() == 50, "Should be equal"
