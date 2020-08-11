from django.contrib.auth.models import User
from django.test import TestCase

from .models import TodoEntry


def test_user():
    user, _ = User.objects.get_or_create(username='John Doe')
    user.set_password('hunter2')
    user.save()
    return user


def test_todo():
    todo, _ = TodoEntry.objects.get_or_create(
        name='test-todo', user=test_user()
    )
    return todo


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


class TestTodoUpdateView(TestCase):

    def setUp(self) -> None:
        self.user = test_user()

    def test_login_required(self):
        test_todo()
        resp = self.client.get(
            '/todo/update/1'
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, '/account/login?next=/todo/update/1')

    def test_update(self):
        # create a new todo entry
        todo = test_todo()

        self.client.login(username='John Doe', password='hunter2')

        resp = self.client.post(
            '/todo/update/1', {'done': "on", "name": todo.name}
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, '/')

        todo = TodoEntry.objects.get(id=todo.id)
        self.assertIs(todo.done, True)
