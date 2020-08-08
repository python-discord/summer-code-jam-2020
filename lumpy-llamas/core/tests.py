import json
from unittest.mock import patch, MagicMock
from django.test import TestCase, Client
from django.http import JsonResponse
from core.helpers import jsonbody


class CoreTestCase(TestCase):

    def test_jsonbody_valid(self):

        schema = {
            'type': 'object',
            'required': ['message'],
            'properties': {
                'message': {
                    'type': 'string',
                    'minLength': 1,
                },
            },
        }

        @jsonbody(schema)
        def view(request, data):
            return JsonResponse({'a': 'b'})

        request = MagicMock()
        request.method = 'POST'
        request.body = json.dumps({'message': 'hello world'}).encode()

        actual = view(request)
        self.assertEqual(actual.status_code, 200)

    def test_jsonbody_invalid(self):

        schema = {
            'type': 'object',
            'required': ['message'],
            'properties': {
                'message': {
                    'type': 'string',
                    'minLength': 1,
                },
            },
        }

        @jsonbody(schema)
        def view(request, data):
            return JsonResponse({'a': 'b'})

        request = MagicMock()
        request.method = 'POST'
        request.body = json.dumps({'stuff': 'things'}).encode()

        actual = view(request)
        self.assertEqual(actual.status_code, 400)

    @patch('core.views.serve')
    def test_index(self, serve):
        client = Client()
        serve.return_value = JsonResponse({'a': 'b'})
        res = client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content.decode(), json.dumps({'a': 'b'}))

    @patch('core.views.login')
    @patch('core.views.User.objects.create_user')
    def test_register(self, c_user, p_login):
        user = MagicMock()
        user.id = 12
        user.username = 'name'
        c_user.return_value = user
        client = Client()

        res = client.post('/api/register', json.dumps({
            'username': 'name',
            'password': 'pass',
        }), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(
            json.loads(res.content.decode()),
            {'username': 'name', 'id': 12},
        )
        c_user.assert_called_with('name', password='pass')
        p_login.assert_called()

    @patch('core.views.login')
    @patch('core.views.authenticate')
    def test_login_success(self, auth, log):
        user = MagicMock()
        user.id = 12
        user.username = 'uname'
        auth.return_value = user
        client = Client()

        res = client.post('/api/login', json.dumps({
            'username': 'name',
            'password': 'pass',
        }), content_type='application/json')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.content.decode()), {
            'username': 'uname',
            'id': 12,
        })

        auth.assert_called()
        log.assert_called()

    @patch('core.views.login')
    @patch('core.views.authenticate')
    def test_login_fail(self, auth, log):
        auth.return_value = None
        client = Client()

        res = client.post('/api/login', json.dumps({
            'username': 'name',
            'password': 'pass',
        }), content_type='application/json')

        self.assertEqual(res.status_code, 401)

        auth.assert_called()
        log.assert_not_called()
