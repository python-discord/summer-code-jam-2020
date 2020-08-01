from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Email, User
# Create your tests here.

class HomePageTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_no_unauthenticated_home_page_access(self):
        """
        If the user is not logged in redirect to login page
        """
        response = self.client.get(reverse("mail:home"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][0], reverse("login"))

    def test_authenticated_user_reaches_inbox(self):
        """
        If the user is authenticated, home should take him to his inbox
        """
        self.client.post(reverse('register'), {'email':'f@f', 'password':'abc','confirmation':'abc'})
        response = self.client.get(reverse("mail:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Inbox")

class RegisterPageTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_register_works(self):
        """
        POST to registration page should create a new user
        """
        response = self.client.post(reverse('register'), {'email':'f@f', 'password':'abc','confirmation':'abc'})
        response2 = self.client.get(reverse('mail:home'))
        self.assertEquals(response2.context['user'].username,'f@f')

    def test_register_passwd_conf_dont_match(self):
        """
        POST to registration page with password and confirmation not matching should should create a new user
        """
        response = self.client.post(reverse('register'), {'email':'f@f', 'password':'abc','confirmation':'abd'})
        self.assertEquals(response.context["message"], "Passwords must match.")

    def test_register_multiple_emails(self):
        """
        POST to registration page with already present user should not go through
        """
        response = self.client.post(reverse('register'), {'email':'f@f', 'password':'abc','confirmation':'abc'})
        response = self.client.post(reverse('register'), {'email':'f@f', 'password':'abc','confirmation':'abc'})
        self.assertEquals(response.context["message"], "Email address already taken.")

    def test_register_get_should_return_webpage(self):
        """
        GET to registration page should return a form
        """
        response = self.client.get(reverse('register'))
        self.assertContains(response, "Register")

