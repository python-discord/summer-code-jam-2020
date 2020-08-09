from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import engine_results


class TestUrls(SimpleTestCase):
    def test_engine_results_url_is_resolved(self):
        url = reverse("engine-results", args=["spaghetti"])

        self.assertEquals(resolve(url).func, engine_results)
