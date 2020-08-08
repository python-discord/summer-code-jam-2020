from django.contrib.auth.models import User
from django.test import TestCase

from .models import TodoEntry


def test_user():
    user, _ = User.objects.get_or_create(username='John Doe')
    user.set_password('hunter2')
    user.save()
    return user


class TestTodoEntry(TestCase):

    def setUp(self) -> None:
        user = test_user()
        self.todo = TodoEntry.objects.create(
            user=user,
            name="Finish summer code jam",
        )

    def test_representation(self):
        self.assertEqual(
            str(self.todo),
            'Finish summer code jam - unfinished'
        )
