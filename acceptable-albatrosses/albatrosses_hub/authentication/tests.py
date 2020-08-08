from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import register_page, login_page, logout_page


class AuthTestCase(TestCase):
    """Class to perform unit tests of auth app."""

    def test_register_url(self):
        response = Client().get(reverse("register_page"))
        self.assertEqual(response.status_code, 200)
    
    def test_login_url(self):
        response = Client().get(reverse("login_page"))
        self.assertEqual(response.status_code, 200)
    
    def test_logout_url(self):
        response = Client().get(reverse("logout_page"))
        self.assertIn(response.status_code, (200, 302))

    def test_register_use_template(self):
        response = Client().get(reverse("register_page"))
        self.assertTemplateUsed(response, "register.html")

    def test_login_use_template(self):
        response = Client().get(reverse("login_page"))
        self.assertTemplateUsed(response, "login.html")

    def test_logout_not_use_template(self):
        response = Client().get(reverse("logout_page"))
        self.assertTemplateNotUsed(response, "logout.html")

    def test_register_using_register_func(self):
        found = resolve(reverse("register_page"))
        self.assertEqual(found.func, register_page)

    def test_login_using_login_func(self):
        found = resolve(reverse("login_page"))
        self.assertEqual(found.func, login_page)

    def test_logout_using_logout_func(self):
        found = resolve(reverse("logout_page"))
        self.assertEqual(found.func, logout_page)
