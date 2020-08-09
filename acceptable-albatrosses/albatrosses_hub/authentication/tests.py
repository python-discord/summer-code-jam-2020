from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from .views import register_page, login_page, logout_page


class AuthTestCase(TestCase):
    """Class to perform unit tests of auth app."""

    def test_register_url(self):
        response = Client().get(reverse("authentication:register"))
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        response = Client().get(reverse("authentication:login"))
        self.assertEqual(response.status_code, 200)

    def test_logout_url(self):
        response = Client().get(reverse("authentication:logout"))
        self.assertIn(response.status_code, (200, 302))

    def test_register_use_template(self):
        response = Client().get(reverse("authentication:register"))
        self.assertTemplateUsed(response, "register.html")

    def test_login_use_template(self):
        response = Client().get(reverse("authentication:login"))
        self.assertTemplateUsed(response, "login.html")

    def test_logout_not_use_template(self):
        response = Client().get(reverse("authentication:logout"))
        self.assertTemplateNotUsed(response, "logout.html")

    def test_register_using_register_func(self):
        found = resolve(reverse("authentication:register"))
        self.assertEqual(found.func, register_page)

    def test_login_using_login_func(self):
        found = resolve(reverse("authentication:login"))
        self.assertEqual(found.func, login_page)

    def test_logout_using_logout_func(self):
        found = resolve(reverse("authentication:logout"))
        self.assertEqual(found.func, logout_page)


class AuthViewTest(TestCase):
    """Class to perform some tests related to views."""

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester", email="test@example.com", password="tester12345")

    def test_logged_in_user_get_redirect_on_register_page(self):
        request = self.factory.get(reverse("authentication:register"))
        request.user = self.user

        response = register_page(request)
        self.assertRedirects(response, "/", fetch_redirect_response=False)

    def test_registered_email_can_not_be_registered(self):
        request = self.factory.post(reverse("authentication:register"))
        request.user = AnonymousUser()
        request.POST = request.POST.copy()
        request.POST["email"] = "test@example.com"

        response = register_page(request)
        self.assertEqual(response.status_code, 200)

    def test_registered_username_can_not_be_taken(self):
        request = self.factory.post(reverse("authentication:register"))
        request.user = AnonymousUser()
        request.POST = request.POST.copy()
        request.POST["email"] = "test2@example.com"
        request.POST["username"] = "tester"

        response = register_page(request)
        self.assertEqual(response.status_code, 200)

    def test_password_is_different_with_retyped_password(self):
        request = self.factory.post(reverse("authentication:register"))
        request.user = AnonymousUser()
        request.POST = request.POST.copy()
        request.POST["email"] = "test2@example.com"
        request.POST["username"] = "tester2"
        request.POST["password"] = "tester2_12345"
        request.POST["re_password"] = "tester_12345"

        response = register_page(request)
        self.assertEqual(response.status_code, 200)

    def test_register_new_user(self):
        request = self.factory.post(reverse("authentication:register"))
        request.user = AnonymousUser()
        request.POST = request.POST.copy()
        request.POST["email"] = "test2@example.com"
        request.POST["username"] = "tester2"
        request.POST["password"] = "tester2_12345"
        request.POST["re_password"] = "tester2_12345"

        response = register_page(request)
        self.assertRedirects(response, reverse("authentication:login"), fetch_redirect_response=False)

    def test_logged_in_user_get_redirect_on_login_page(self):
        request = self.factory.get(reverse("authentication:login"))
        request.user = self.user

        response = login_page(request)
        self.assertRedirects(response, "/", fetch_redirect_response=False)

    def test_username_is_not_registered(self):
        request = self.factory.post(reverse("authentication:login"))
        request.user = AnonymousUser()
        request.POST = request.POST.copy()
        request.POST["username"] = "no_name"

        response = login_page(request)
        self.assertEqual(response.status_code, 200)

    def test_wrong_password(self):
        request = self.factory.post(reverse("authentication:login"))
        request.user = AnonymousUser()
        request.POST = request.POST.copy()
        request.POST["username"] = "tester"
        request.POST["password"] = "idunnomypassword"

        response = login_page(request)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        request = self.factory.post(reverse("authentication:login"))
        request.user = AnonymousUser()
        request.POST = request.POST.copy()
        request.POST["username"] = "tester"
        request.POST["password"] = "tester12345"

        response = login_page(request)
        self.assertRedirects(response, "/", fetch_redirect_response=False)

    def test_anonymous_user_can_not_access_logout_page(self):
        request = self.factory.get(reverse("authentication:logout"))
        request.user = AnonymousUser()

        response = logout_page(request)
        self.assertRedirects(response, "/", fetch_redirect_response=False)

    def test_logout(self):
        request = self.factory.post(reverse("authentication:logout"))
        request.user = self.user

        response = logout_page(request)
        self.assertRedirects(response, "/", fetch_redirect_response=False)
