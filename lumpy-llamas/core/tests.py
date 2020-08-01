import json
from unittest.mock import patch
from django.test import TestCase, Client
from django.http import JsonResponse


class CoreTestCase(TestCase):

    @patch('core.views.serve')
    def test_index(self, serve):
        client = Client()
        serve.return_value = JsonResponse({'a': 'b'})
        res = client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content.decode(), json.dumps({'a': 'b'}))
