from django.test import TestCase
import io
import base64


USERNAME = 'haha69420'
PASSWORD = 'foobar < xyzzy'


# FIXME: NAME TBD
class TestStuff(TestCase):
    def setUp(self):
        # we create an account with the `USERNAME` and `PASSWORD` vars
        params = {
            'username': USERNAME,
            'email': 'foo@example.com',
            'password1': PASSWORD,
            'password2': PASSWORD
        }

        self.client.post('/users/register', params)
        self.client.login(username=USERNAME, password=PASSWORD)

    def test_register_and_home(self):
        # assumptions (aka what this tests):
        #  - `/user/register` exists.
        #  - it takes certain params.
        #  - it also logs us in.
        #  - `/` exists.
        #  - it tells us our username.
        #  - we use django's built-in auth system.

        res = self.client.get('/').content
        self.assertIn(USERNAME.encode(), res, 'Our username does not appear in the home view.')

        self.client.logout()
        res = self.client.get('/').content

        self.assertNotIn(USERNAME.encode(), res, 'Our username was already in the home view.')

    def test_upload_templates(self):
        # what this assumes:
        # - the above tests go through
        # - when you create a page the
        #   available templates are
        #   passed in. and in a certain
        #   way.
        # - posting `/templates/new`
        #   creates a specified template

        # example stylesheet
        style = io.StringIO('body { display: hidden; }')
        template_name = 'blahblahblah'

        res = self.client.get('/pages/new')
        template_entries = [entry[1] for entry in res.context['form'].fields['template_used'].choices]
        self.assertNotIn(template_name, template_entries)

        self.client.post('/templates/new', {'name': template_name, 'style_sheet': style})

        res = self.client.get('/pages/new')
        template_entries = [entry[1] for entry in res.context['form'].fields['template_used'].choices]
        self.assertIn(template_name, template_entries)
