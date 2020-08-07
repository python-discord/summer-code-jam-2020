from django.test import TestCase
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from pathlib import Path
import io
import base64

from .models import User, Webpage, Template, Comment
from .forms import CommentForm

USERNAME = 'haha69420'
PASSWORD = 'foobar < xyzzy'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'hard123passwd'


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
    fixtures = ['users.yaml', 'templates.yaml', 'webpages.yaml', 'comments.yaml']

    def test_webpage_create_redirect(self):
        res = self.client.get('/pages/new')
        self.assertRedirects(res, '/users/login?next=/pages/new')

    def test_webpage_create(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.get('/pages/new')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, template_name='page_maker/webpage_create.html')
        image_path = Path(settings.BASE_DIR) / 'test_media' / 'images' / 'test.png'
        image1 = SimpleUploadedFile(name='test.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        image2 = SimpleUploadedFile(name='test.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        image3 = SimpleUploadedFile(name='test.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        image4 = SimpleUploadedFile(name='test.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        form_input = {
            'name': 'asdf',
            'template_used': '1',
            'user_title': 'ASDF',
            'user_text_1': 'zxcvasdfqwer',
            'user_text_2': 'zxcvasdfqwer',
            'user_text_3': 'zxcvasdfqwer',
            'user_image_1': image1,
            'user_image_2': image2,
            'user_image_3': image3,
            'user_image_4': image4,
        }
        res = self.client.post('/pages/new', form_input)
        self.assertRedirects(res, '/pages/asdf/')
        self.assertEqual(Webpage.objects.count(), 2)
        webpage = Webpage.objects.get(pk=2)
        self.assertEqual(webpage.name, form_input['name'])

    def test_webpage_preview(self):
        res = self.client.get('/pages/mypage/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'page_maker/webpage_view.html')
        self.assertIsInstance(res.context['webpage'], Webpage)
        self.assertEqual(res.context['webpage'].user_title, 'thats my page')

    def test_webpage_detail(self):
        res = self.client.get('/pages/mypage/detail')
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['comment_form'], CommentForm)
        self.assertIsInstance(res.context['comments'][0], Comment)

    def test_webpage_list(self):
        res = self.client.get('/pages/')
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['webpages'][0], Webpage)

    def test_webpage_update(self):
        self.client.login(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
        res = self.client.get('/pages/mypage/update')
        self.assertEqual(res.status_code, 200)
        webpage = Webpage.objects.get(pk=1)
        form_data = webpage.__dict__
        form_data['user_title'] = 'abcd test 01234'
        form_data['template_used'] = '1'
        res = self.client.post('/pages/mypage/update', form_data)
        self.assertRedirects(res, '/pages/mypage/')
        webpage = Webpage.objects.get(pk=1)
        self.assertEqual(webpage.user_title, 'abcd test 01234')

    def test_webpage_delete(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post('/pages/mypage/delete')
        self.assertEqual(res.status_code, 403)
        self.client.login(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
        res = self.client.post('/pages/mypage/delete')
        self.assertRedirects(res, '/')
        self.assertEqual(Webpage.objects.count(), 0)


class TemplateViewsTest(TestCase):
    fixtures = ['users.yaml', 'templates.yaml']

    def setUp(self):
        self.client.login(username=USERNAME, password=PASSWORD)

    def test_template_create(self):
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

    def test_template_detail(self):
        res = self.client.get('/templates/1/')
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['template'], Template)

    def test_template_list(self):
        res = self.client.get('/templates/')
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['templates'][0], Template)

    def test_template_delete(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post('/templates/1/delete')
        self.assertEqual(res.status_code, 403)
        self.client.login(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
        res = self.client.post('/templates/1/delete')
        self.assertRedirects(res, '/')
        self.assertEqual(Template.objects.count(), 1)


class CommentViewsTest(TestCase):
    fixtures = ['users.yaml', 'webpages.yaml', 'templates.yaml', 'comments.yaml']

    def test_comment_create(self):
        form_data = {
            'title': 'test comment',
            'content': 'another test'
        }
        res = self.client.post('/pages/mypage/comment', form_data)
        self.assertRedirects(res, '/users/login?next=/pages/mypage/detail')
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post('/pages/mypage/comment', form_data)
        self.assertRedirects(res, '/pages/mypage/detail')
        self.assertEqual(Comment.objects.count(), 3)

    def test_comment_delete(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post('/comments/1/delete')
        self.assertEqual(res.status_code, 403)
        self.client.login(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
        res = self.client.post('/comments/1/delete')
        self.assertRedirects(res, '/pages/mypage/detail')
        self.assertEqual(Template.objects.count(), 1)
