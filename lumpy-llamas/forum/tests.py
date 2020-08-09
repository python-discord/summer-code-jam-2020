import json
from django.test import TestCase, Client
from django.contrib.auth.models import User
from unittest.mock import patch
from django.http import JsonResponse

from .models import Thread, ThreadMessage


class ThreadTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="testuser", id=12)
        Thread.objects.create(title="test title", created_by=user)

    def test_title_label(self):
        thread = Thread.objects.get(id=1)
        field_label = thread._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        thread = Thread.objects.get(id=1)
        max_length = thread._meta.get_field('title').max_length
        self.assertEquals(max_length, 120)

    def test_str_representation(self):
        thread = Thread.objects.get(id=1)
        expected_object_name = thread.title
        self.assertEquals(expected_object_name, str(thread))


class ThreadMessageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="testuser", id=12)
        thread = Thread.objects.create(title="test title", created_by=user)
        ThreadMessage.objects.create(thread=thread, user=user, message="testmessage")

    def test_message_label(self):
        message = ThreadMessage.objects.get(id=1)
        field_label = message._meta.get_field('message').verbose_name
        self.assertEquals(field_label, 'message')

    def test_message_max_length(self):
        message = ThreadMessage.objects.get(id=1)
        max_length = message._meta.get_field('message').max_length
        self.assertEquals(max_length, 3000)

    def test_str_representation(self):
        message = ThreadMessage.objects.get(id=1)
        expected_object_name = f'Message by {message.user} created {message.date} | {message.message}'
        self.assertEquals(expected_object_name, str(message))


class ForumViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser")
        cls.user.set_password('password')
        cls.user.save()
        cls.thread = Thread.objects.create(title="test title", created_by=cls.user)
        cls.message = ThreadMessage.objects.create(thread=cls.thread, user=cls.user, message="testmessage")
        cls.client = Client()

    @patch('core.views.serve')
    def test_thread_list_view(self, serve):
        serve.return_value = JsonResponse({'title': self.thread.title})
        res = self.client.get('/api/forum')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content.decode(), json.dumps({'title': 'test title'}))

    @patch('core.views.serve')
    def test_thread_details_view(self, serve):
        serve.return_value = JsonResponse({'title': self.thread.title, 'message': self.message.message})
        res = self.client.get(f'/api/forum/{self.thread.id}/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content.decode(), json.dumps({'title': 'test title', 'message': 'testmessage'}))

    def test_post_thread_view(self):
        self.client.login(username=self.user.username, password='password')

        res = self.client.post('/api/forum/post/thread', json.dumps({
            'title': 'title',
            'message': 'message',
        }), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(
            json.loads(res.content.decode()),
            {'thread_id': self.thread.id + 1, 'message': 'message', 'user': 'testuser'},
        )

    def test_post_message_view(self):
        self.client.login(username=self.user.username, password='password')
        res = self.client.post('/api/forum/post/message', json.dumps({
            'message': 'message',
            'user': self.user.username,
            'thread_id': self.thread.id
        }), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(
            json.loads(res.content.decode()),
            {'thread_id': self.thread.id, 'message': 'message', 'user': 'testuser'},
        )
