from django.test import TestCase, Client


USERNAME = 'abcdef'


class TestUserRegistration(TestCase):
    def test_register_and_home(self):
        # assumptions (aka what this tests):
        #  - `/user/register` exists.
        #  - it takes certain params.
        #  - it also logs us in.
        #  - `/` exists.
        #  - it tells us our username.
        #  - we use django's built-in auth system.

        # we don't want to leak our
        # signed in user to other
        # tests that might be running
        client = Client()
        password = 'foobar < xyzzy'

        params = {
            'username': 'foo',
            'email': 'foo@bar.com',
            'password1': password,
            'password2': password
        }

        # note(a5): it seems the following POST request does
        #   not set the user credentials?
        client.post('/users/register', params, follow=True)
        client.login(username='foo', password=password)
        res = client.get('/').content

        self.assertIn(b'foo', res, 'Our username does not appear in the home view.')

        client.logout()
        res = client.get('/').content

        self.assertNotIn(b'foo', res, 'Our username was already in the home view.')
