from pathlib import Path

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .forms import CommentForm
from .models import User, Webpage, Template, Comment

USERNAME = 'haha69420'
PASSWORD = 'foobar < xyzzy'
EMAIL = 'foo@example.com'

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'hard123passwd'


class UserRegisterTest(TestCase):
    def setUp(self):
        # we create an account with the `USERNAME` and `PASSWORD` vars
        params = {
            'username': USERNAME,
            'email': EMAIL,
            'password1': PASSWORD,
            'password2': PASSWORD
        }

        self.client.post(reverse('register'), params)
        self.client.login(username=USERNAME, password=PASSWORD)

    def test_user_exists(self):
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, USERNAME)
        self.assertEqual(user.email, EMAIL)

    def test_register_and_home(self):
        """
        Assumptions (AKA what this integration test tests):
         - `/user/register` exists.
         - ^ takes certain params.
         - ^ also logs us in.
         - `/` exists.
         - ^ tells us our username.
         - We are using django's built-in auth system.
        """

        res = self.client.get('/').content
        self.assertIn(USERNAME.encode(), res, 'Our username does not appear in the home view.')

        self.client.logout()
        res = self.client.get('/').content

        self.assertNotIn(USERNAME.encode(), res, 'Our username was already in the home view.')


class UserViewsTest(TestCase):
    fixtures = ['users.yaml', 'webpages.yaml', 'templates.yaml']

    def test_user_detail(self):
        user = User.objects.get(pk=1)
        res = self.client.get(reverse('user-detail', kwargs={'pk': 1}))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['viewed_user'], user)
        self.assertIsInstance(res.context['user_pages'][0], Webpage)

    def test_user_update(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post(reverse('user-update', kwargs={'pk': 1}), {
            'first_name': 'john', 'last_name': 'lemon', 'email': 'jl@sth.com'
        })
        self.assertEqual(res.status_code, 403)
        res = self.client.post(reverse('user-update', kwargs={'pk': 2}), {
            'first_name': 'john', 'last_name': 'lemon', 'email': 'jl@sth.com'
        })
        self.assertRedirects(res, '/')
        user = User.objects.get(pk=2)
        self.assertEqual(user.last_name, 'lemon')

    def test_user_delete(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post(reverse('user-delete', kwargs={'pk': 2}))
        self.assertRedirects(res, '/')
        self.assertEqual(User.objects.count(), 1)


class WebpageViewsTest(TestCase):
    fixtures = ['users.yaml', 'templates.yaml', 'webpages.yaml', 'comments.yaml']

    def test_webpage_create_redirect(self):
        res = self.client.get(reverse('webpage-create'))
        self.assertRedirects(res, reverse('login') + '?next=' + reverse('webpage-create'))

    def test_webpage_create(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.get(reverse('webpage-create'))
        self.assertEqual(res.status_code, 200)
        image_path = Path(settings.BASE_DIR) / 'test_media' / 'images' / 'test.png'
        image1 = SimpleUploadedFile(name='test.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        image2 = SimpleUploadedFile(name='test.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        image3 = SimpleUploadedFile(name='test.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')
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
        }
        res = self.client.post(reverse('webpage-create'), form_input)
        self.assertRedirects(res, reverse('webpage-view', kwargs={'pagename': 'asdf'}))
        self.assertEqual(Webpage.objects.count(), 2)
        webpage = Webpage.objects.get(pk=2)
        self.assertEqual(webpage.name, form_input['name'])

    def test_webpage_preview(self):
        res = self.client.get(reverse('webpage-view', kwargs={'pagename': 'mypage'}))
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['webpage'], Webpage)
        self.assertEqual(res.context['webpage'].user_title, 'thats my page')

    def test_webpage_detail(self):
        res = self.client.get(reverse('webpage-detail', kwargs={'pagename': 'mypage'}))
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['comment_form'], CommentForm)
        self.assertIsInstance(res.context['comments'][0], Comment)

    def test_webpage_list(self):
        res = self.client.get(reverse('webpage-list'))
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['webpages'][0], Webpage)

    def test_webpage_update(self):
        self.client.login(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
        res = self.client.get(reverse('webpage-update', kwargs={'pagename': 'mypage'}))
        self.assertEqual(res.status_code, 200)
        webpage = Webpage.objects.get(pk=1)
        form_data = webpage.__dict__
        form_data['user_title'] = 'abcd test 01234'
        form_data['template_used'] = '1'
        res = self.client.post(reverse('webpage-update', kwargs={'pagename': 'mypage'}), form_data)
        self.assertRedirects(res, reverse('webpage-view', kwargs={'pagename': 'mypage'}))
        webpage = Webpage.objects.get(pk=1)
        self.assertEqual(webpage.user_title, 'abcd test 01234')

    def test_webpage_delete(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post(reverse('webpage-delete', kwargs={'pagename': 'mypage'}))
        self.assertEqual(res.status_code, 403)
        self.client.login(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
        res = self.client.post(reverse('webpage-delete', kwargs={'pagename': 'mypage'}))
        self.assertRedirects(res, '/')
        self.assertEqual(Webpage.objects.count(), 0)


class TemplateViewsTest(TestCase):
    fixtures = ['users.yaml', 'templates.yaml']

    def setUp(self):
        self.client.login(username=USERNAME, password=PASSWORD)

    def test_template_create(self):
        """
        What this assumes:
         - When you create a page the
           available templates are
           passed in. and in a certain
           way.
         - POST-ing `/templates/new`
           creates a specified template
         - The console theme exists.
        """

        # example stylesheet
        template_name = 'blahblahblah'
        style = str(Path(settings.MEDIA_ROOT) / 'static' / 'themes' / 'console.css')

        res = self.client.get(reverse('webpage-create'))
        template_entries = [entry[1] for entry in res.context['form'].fields['template_used'].choices]
        self.assertNotIn(template_name, template_entries)

        self.client.post(reverse('template-create'), {'name': template_name, 'style_sheet': style})

        res = self.client.get(reverse('webpage-create'))
        template_entries = [entry[1] for entry in res.context['form'].fields['template_used'].choices]
        self.assertIn(template_name, template_entries)

    def test_template_detail(self):
        res = self.client.get(reverse('template-detail', kwargs={'templatename': self.template_name}))
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['template'], Template)

    def test_template_list(self):
        res = self.client.get(reverse('template-list'))
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.context['templates'][0], Template)

    def test_template_delete(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post(reverse('template-delete', kwargs={'templatename': self.template_name}))
        self.assertEqual(res.status_code, 403)
        self.client.login(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
        res = self.client.post(reverse('template-delete', kwargs={'templatename': self.template_name}))
        self.assertRedirects(res, '/')
        self.assertEqual(Template.objects.count(), 1)


class CommentViewsTest(TestCase):
    fixtures = ['users.yaml', 'webpages.yaml', 'templates.yaml', 'comments.yaml']

    def test_comment_create(self):
        form_data = {
            'title': 'test comment',
            'content': 'another test'
        }
        res = self.client.post(reverse('comment-create', kwargs={'pagename': 'mypage'}), form_data)
        self.assertRedirects(
            res, reverse('login') + '?next=' + reverse('webpage-detail', kwargs={'pagename': 'mypage'})
        )
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post(reverse('comment-create', kwargs={'pagename': 'mypage'}), form_data)
        self.assertRedirects(res, reverse('webpage-detail', kwargs={'pagename': 'mypage'}))
        self.assertEqual(Comment.objects.count(), 3)

    def test_comment_delete(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        res = self.client.post(reverse('comment-delete', kwargs={'pk': 1}))
        self.assertEqual(res.status_code, 403)
        self.client.login(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
        res = self.client.post(reverse('comment-delete', kwargs={'pk': 1}))
        self.assertRedirects(res, reverse('webpage-detail', kwargs={'pagename': 'mypage'}))
        self.assertEqual(Comment.objects.count(), 1)
