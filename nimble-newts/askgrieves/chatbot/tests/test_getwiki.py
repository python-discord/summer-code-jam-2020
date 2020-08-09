from django.http import JsonResponse

import pytest


@pytest.mark.django_db
def test_getwiki_json(client, db):
    resp = client.post('/getwiki/', {'article_name': 'Django (web framework)'})
    assert isinstance(resp, JsonResponse)


@pytest.mark.django_db
def test_getwiki_404(client, db):
    resp = client.post('/getwiki/', {'article_name': "A Page that doesn't exist"})
    assert resp.status_code == 404
