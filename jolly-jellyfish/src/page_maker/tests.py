from django.test import TestCase
import io
import base64

from .models import User, Webpage, Template

USERNAME = 'haha69420'
PASSWORD = 'foobar < xyzzy'


class UserRegisterTest(TestCase):
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

    def test_user_exists(self):
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, USERNAME)

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


class UserViewsTest(TestCase):
    fixtures = ['users.yaml', 'webpages.yaml', 'templates.yaml']

    def test_user_detail(self):
        user = User.objects.get(pk=1)
        res = self.client.get('/users/1/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['viewed_user'], user)
        self.assertIsInstance(res.context['user_pages'][0], Webpage)

    def test_user_update(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post('/users/2/update', {
            'first_name': 'john', 'last_name': 'lemon', 'email': 'jl@sth.com'
        })
        self.assertRedirects(res, '/')
        user = User.objects.get(pk=2)
        self.assertEqual(user.last_name, 'lemon')

    def test_user_delete(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post('/users/2/delete')
        self.assertRedirects(res, '/')
        self.assertEqual(User.objects.count(), 1)


class WebpageViewsTest(TestCase):
    fixtures = ['users.yaml']

    def test_webpage_create(self):
        pass

    def test_webpage_preview(self):
        # TODO test if proper theme is loaded
        # TODO test if user data is inside
        pass

    def test_webpage_detail(self):
        # TODO check if form and comments are in context
        pass

    def test_webpage_list(self):
        pass

    def test_webpage_update(self):
        pass

    def test_webpage_delete(self):
        # TODO test delete permissions
        pass


class TemplateViewsTest(TestCase):
    fixtures = ['users.yaml']

    def setUp(self):
        self.client.login(username=USERNAME, password=PASSWORD)

    def test_upload_templates(self):
        # what this assumes:
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
