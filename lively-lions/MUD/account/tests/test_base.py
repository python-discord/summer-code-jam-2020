from django.contrib.auth.models import User
from django.test import TestCase
import pytest
from mixer.backend.django import mixer


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
