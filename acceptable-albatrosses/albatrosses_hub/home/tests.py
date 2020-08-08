from django.test import TestCase, Client


class HomeTestCase(TestCase):
    """Class to perform unit tests of home app."""

    def test_home_url(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_use_template(self):
        response = Client().get("/")
        self.assertTemplateUsed(response, "home.html")
