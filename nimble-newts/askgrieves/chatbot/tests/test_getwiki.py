from django.http import JsonResponse

import pytest

import json


@pytest.mark.django_db
class TestWiki:
    @pytest.fixture
    def django_wiki(self, client):
        return client.post('/getwiki/', {'article_name': 'Django (web framework)'})

    def test_getwiki_json(self, django_wiki):
        """Check if a JSON response is sent."""
        assert isinstance(django_wiki, JsonResponse)

    def test_getwiki_structure(self, django_wiki):
        """Verify the JSON structure."""
        article = json.loads(django_wiki.content)
        assert set(['name', 'summary']) == set(article.keys())

    def test_getwiki_content(self, django_wiki):
        """Verify the content in the JSON response."""
        assert 'Python-based' in django_wiki.content.decode()

    def test_getwiki_404(self, client):
        """Check if non-existent pages result in 404."""
        resp = client.post('/getwiki/', {'article_name': "A Page that doesn't exist"})
        assert resp.status_code == 404
