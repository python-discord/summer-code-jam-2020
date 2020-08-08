from django.contrib.auth.models import User
from django.test import TestCase, Client

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


class TestTodoCreateView(TestCase):

    def setUp(self) -> None:
        self.user = test_user()

    def test_login_required(self):
        resp = self.client.get(
            '/todo/add/'
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, '/account/login?next=/todo/add/')

    def test_add_entry(self):
        logged_in = self.client.login(username='John Doe', password='hunter2')
        self.assertEqual(logged_in, True)

        resp = self.client.post(
            '/todo/add/', {'name': 'test-todo-entry'}
        )

        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, '/')

        created = TodoEntry.objects.get(name='test-todo-entry')
        self.assertIsNotNone(created)
        self.assertEqual(created.user, self.user)
