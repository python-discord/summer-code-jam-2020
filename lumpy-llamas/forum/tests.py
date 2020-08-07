from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from .models import Thread, ThreadMessage


# #models test
class ModelsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.thread = Thread.objects.create(title="A thread title", created_by=self.user)
        self.message = ThreadMessage.objects.create(thread=self.thread, created_by=self.user)

    def test_thread_has_slug(self):
        pass

