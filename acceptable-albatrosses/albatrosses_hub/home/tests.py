from django.test import TestCase, Client
from django.urls import resolve
from .views import homepage, about_us


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
        self.assertTemplateUsed(response, "home.html")
    
    def test_about_us_use_template(self):
        response = Client().get("/about-us/")
        self.assertTemplateUsed(response, "about.html")

    def test_home_using_home_func(self):
        found = resolve("/")
        self.assertEqual(found.func, homepage)

    def test_about_us_using_about_us_func(self):
        found = resolve("/about-us/")
        self.assertEqual(found.func, about_us)


class HomeViewTest(TestCase):
    """Class to perform some tests related to views."""

    def test_logged_in_user_access_home(self):
        session = self.client.session
        session["email"] = "test@example.com"
        session.save()

        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_anonymous_user_access_home(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

