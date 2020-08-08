from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from .models import Thread, ThreadMessage
from django.http import JsonResponse


# #models test
class ModelsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.thread = Thread.objects.create(title="A thread title", created_by=self.user)
        self.message = ThreadMessage.objects.create(thread=self.thread, created_by=self.user)

    def test_thread_has_slug(self):
        pass


class TestPostThread(TestCase):
    def test_can_send_message(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        data = {
            "title": "Test thread",
            "user":  self.user,
            "message": "Would love to talk about Philip K. Dick",
        }
        response = self.client.get("/contact/")
        self.assertTemplateUsed(response, "library/contact_form.html")
        self.assertContains(response,"first_name")
        self.assertContains(response, "last_name")
        response = self.client.post("/contact/", data=data)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertRedirects(response, "/thanks/")