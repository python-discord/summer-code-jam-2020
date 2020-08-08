from django.contrib.auth.models import User
from django.test import TestCase
import pytest
from mixer.backend.django import mixer
from dungeon.models.character import MudUser
from django.db import IntegrityError


@pytest.mark.django_db
class TestBaseTest(TestCase):
    def test_smoke_test(self):
        assert 1 == 1, "Should be equal"

    def test_001_create_user_model(self):
        """
        # For Debug
        # pytest --pdb
        # pytest.set_trace()
        """
        user = User.objects.create(
            username='Hello_World')
        assert User.objects.count() == 1, "Should be equal"
        assert User.objects.get(pk=1).username == user.username, "Should be equal"

    def test_002_create_user_with_mixer(self):
        user = mixer.blend(User)
        assert User.objects.count() == 1, "Should be equal"
        assert User.objects.get(pk=1).username == user.username, "Should be equal"

    def test_003_create_many_user_with_mixer(self):
        for i in range(50):
            user = mixer.blend(User)
            assert User.objects.get(pk=i+1).username == user.username, "Should be equal"
        assert User.objects.count() == 50, "Should be equal"

    def test_004_create_muduser_model(self):
        user = MudUser.objects.create(
            username='Hello_World')
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == user.username, "Should be equal"

    def test_004_01_create_muduser_model_with_password(self):
        user = MudUser.objects.create(
                username='Hello_World',
                password='Hello_World',
                )
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == user.username, "Should be equal"
        assert MudUser.objects.get(pk=1).password == user.password, "Should be equal"

    def test_004_02_create_same_two_username_muduser_model_with_password(self):
        try:
            user1 = MudUser.objects.create(
                    username='Hello_World',
                    password='Hello_World01',
                    )
            user2 = MudUser(
                        username='Hello_World',
                        password='Hello_World02')
        except IntegrityError:
            pass

        with self.assertRaises(MudUser.DoesNotExist):
            assert MudUser.objects.get(pk=2).username == user2.username, "Should be equal"
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == user1.username, "Should be equal"
        assert MudUser.objects.get(pk=1).password == user1.password, "Should be equal"

    def test_004_02_create_muduser_model_wtih_muduser_method(self):
        user = MudUser(username='Hello_World', password='Hello_World')
        user.save()
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == user.username, "Should be equal"

    def test_005_create_muduser_with_mixer(self):
        user = mixer.blend(MudUser)
        assert MudUser.objects.count() == 1, "Should be equal"
        assert MudUser.objects.get(pk=1).username == user.username, "Should be equal"

    def test_006_create_many_muduser_with_mixer(self):
        for i in range(50):
            user = mixer.blend(MudUser)
            assert MudUser.objects.get(pk=i+1).username == user.username, "Should be equal"
        assert MudUser.objects.count() == 50, "Should be equal"
