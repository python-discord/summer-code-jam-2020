import json
from unittest.mock import patch, MagicMock
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
