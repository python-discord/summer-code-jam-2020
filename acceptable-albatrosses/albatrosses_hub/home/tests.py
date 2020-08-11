from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from django.urls import resolve

from .views import index, about_us


class HomeTestCase(TestCase):
    """Class to perform unit tests of home app."""

    def test_home_url(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_us_url(self):
        response = Client().get("/about-us/")
        self.assertEqual(response.status_code, 200)

    def test_home_use_template(self):
        response = Client().get("/")
        self.assertTemplateUsed(response, "home/index.html")

    def test_about_us_use_template(self):
        response = Client().get("/about-us/")
        self.assertTemplateUsed(response, "home/about.html")

    def test_home_using_home_func(self):
        found = resolve("/")
        self.assertEqual(found.func, index)

    def test_about_us_using_about_us_func(self):
        found = resolve("/about-us/")
        self.assertEqual(found.func, about_us)


class HomeViewTest(TestCase):
    """Class to perform some tests related to views."""

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester", email="test@example.com", password="tester12345")

    def test_logged_in_user_access_home(self):
        request = self.factory.get("/")
        request.user = self.user

        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_anonymous_user_access_home(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)
