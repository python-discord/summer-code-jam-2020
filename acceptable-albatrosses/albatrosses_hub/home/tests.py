from django.test import TestCase, Client
from django.urls import resolve
from .views import homepage


class HomeTestCase(TestCase):
    """Class to perform unit tests of home app."""

    def test_home_url(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_use_template(self):
        response = Client().get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_home_using_home_func(self):
        found = resolve("/")
        self.assertEqual(found.func, homepage)
