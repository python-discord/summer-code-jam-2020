from django.contrib.auth.models import User
from django.test import TestCase

from .models import TodoEntry


class TodoEntryTest(TestCase):

    def setUp(self) -> None:
        user = User.objects.create(
            username='John Doe',
            password='hunter2'
        )
        self.todo = TodoEntry.objects.create(
            user=user,
            name="Finish summer code jam",
        )

    def test_representation(self):
        self.assertEqual(
            str(self.todo),
            'Finish summer code jam - unfinished'
        )
