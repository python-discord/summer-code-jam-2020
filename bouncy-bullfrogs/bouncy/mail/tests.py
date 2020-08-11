from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Email, User
import json
# Create your tests here.


class HomePageTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_no_unauthenticated_home_page_access(self):
        """
        If the user is not logged in redirect to login page
        """
        response = self.client.get(reverse("mail:home"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][0], reverse("login"))

    def test_authenticated_user_reaches_inbox(self):
        """
        If the user is authenticated, home should take him to his inbox
        """
        self.client.post(reverse('register'), {
                         'email': 'f@f', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse("mail:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Inbox")


class RegisterPageTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_register_works(self):
        """
        POST to registration page should create a new user
        """
        response2 = self.client.get(reverse('mail:home'))
        self.assertEquals(response2.context['user'].username, 'f@f')

    def test_register_passwd_conf_dont_match(self):
        """
        POST to registration page with password and confirmation not matching
        should should create a new user
        """
        response = self.client.post(reverse('register'), {
                                    'email': 'f@f', 'password': 'abc',
                                    'confirmation': 'abd'})
        self.assertEquals(response.context["message"], "Passwords must match.")

    def test_register_multiple_emails(self):
        """
        POST to registration page with already present user should
        not go through
        """
        response = self.client.post(reverse('register'),
                                    {
                                    'email': 'f@f', 'password': 'abc',
                                    'confirmation': 'abc'})
        response = self.client.post(reverse('register'), {
                                    'email': 'f@f', 'password': 'abc',
                                    'confirmation': 'abc'})
        self.assertEquals(
            response.context["message"], "Email address already taken.")

    def test_register_get_should_return_webpage(self):
        """
        GET to registration page should return a form
        """
        response = self.client.get(reverse('register'))
        self.assertContains(response, "Register")


class ComposingEmailTests(TestCase):
    def setup(self):
        self.client = Client()

    def create_users(self):
        self.client.post(reverse('register'), {
                         'email': 'c@c', 'password': 'abc',
                         'confirmation': 'abc'})
        self.client.logout()
        self.client.post(reverse('register'), {
                         'email': 'a@a', 'password': 'abc',
                         'confirmation': 'abc'})
        self.client.logout()

    def test_request_should_be_post(self):
        """
        The request should be POST
        """
        self.client.post(reverse('register'), {
                         'email': 'b@b', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get('/emails')
        self.assertEquals(json.loads(response.content)[
                          'error'], 'POST request required.')

    def test_no_recepients_should_give_error(self):
        """
        Request with no receipients should give error
        """
        self.client.post(reverse('register'), {
                         'email': 'b@b', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.post('/emails', json.dumps(
            {'recipients': '', 'subject': 'test', 'body': 'test'}),
            content_type='application/json')
        self.assertEquals(json.loads(response.content)[
                          'error'], "At least one recipient required.")

    def test_invalid_recepients_should_give_error(self):
        """
        Request with invalid receipients should give error
        """
        self.create_users()
        self.client.post(reverse('register'), {
                         'email': 'b@b', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.post('/emails', json.dumps(
            {'recipients': 'l@l', 'subject': 'test', 'body': 'test'}),
            content_type='application/json')
        self.assertEquals(json.loads(response.content)[
                          'error'], "User with email l@l does not exist.")

    def test_valid_request_should_work(self):
        """
        Request with invalid receipients should give error
        """
        self.create_users()
        self.client.post(reverse('register'), {
                         'email': 'b@b', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.post('/emails', json.dumps(
            {'recipients': 'a@a, c@c', 'subject': 'test', 'body': 'test'}),
            content_type='application/json')
        self.assertEquals(json.loads(response.content)[
                          'message'], "Email sent successfully.")


class MailboxTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_inbox_shows_received_mails(self):
        """
        Email sent to a user must appear in inbox
        """
        self.client.post(reverse('register'), {
                         'email': 'a@a', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse('mail:home'))
        user1 = User.objects.get(username=response.context['user'].username)
        self.client.logout()
        self.client.post(reverse('register'), {
                         'email': 'b@b', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse('mail:home'))
        user3 = User.objects.get(username=response.context['user'].username)
        # user1 --> user3
        email = Email(
            user=user3,
            sender=user1,
            subject="Test",
            body="Test",
            read=False,
        )
        email.save()
        email.recipients.add(user3)
        email.save()
        response = self.client.get(
            reverse('mail:mailbox', kwargs={'mailbox': "inbox"}))
        self.assertEqual(json.loads(response.content)[0], email.serialize())

    def test_sent_shows_sent_mails(self):
        """
        Email sent by a user must appear in sent
        """
        self.client.post(reverse('register'), {
                         'email': 'a@a', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse('mail:home'))
        user1 = User.objects.get(username=response.context['user'].username)
        self.client.logout()
        self.client.post(reverse('register'), {
                         'email': 'b@b', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse('mail:home'))
        user3 = User.objects.get(username=response.context['user'].username)
        # user3 --> user1
        email = Email(
            user=user3,
            sender=user3,
            subject="Test",
            body="Test",
            read=True,
        )
        email.save()
        email.recipients.add(user1)
        email.save()
        response = self.client.get(
            reverse('mail:mailbox', kwargs={'mailbox': "sent"}))
        self.assertEqual(json.loads(response.content)[0], email.serialize())

    def test_archive_shows_archived_mails(self):
        """
        Email archived by a user must appear in archived and not in inbox
        """
        self.client.post(reverse('register'), {
                         'email': 'a@a', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse('mail:home'))
        user1 = User.objects.get(username=response.context['user'].username)
        self.client.logout()
        self.client.post(reverse('register'), {
                         'email': 'b@b', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse('mail:home'))
        user3 = User.objects.get(username=response.context['user'].username)
        # user1 --> user3
        email = Email(
            user=user3,
            sender=user1,
            subject="Test",
            body="Test",
            read=True,
            archived=True
        )
        email.save()
        email.recipients.add(user3)
        email.save()
        response = self.client.get(
            reverse('mail:mailbox', kwargs={'mailbox': "archive"}))
        self.assertEqual(json.loads(response.content)[0], email.serialize())

        # user1 --> user3
        email = Email(
            user=user3,
            sender=user1,
            subject="Test",
            body="Test",
            read=True,
            archived=True
        )
        email.save()
        email.recipients.add(user3)
        email.save()
        response = self.client.get(
            reverse('mail:mailbox', kwargs={'mailbox': "inbox"}))
        self.assertEquals(json.loads(response.content), [])

    def test_invalid_mailbox_name_gives_error(self):
        """
        Invalid Inbox name must give an error
        """
        self.client.post(reverse('register'), {
                         'email': 'b@b', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse('mail:home'))
        response = self.client.get(
            reverse('mail:mailbox', kwargs={'mailbox': "abracadabra"}))
        self.assertEquals(json.loads(response.content)[
                          'error'], 'Invalid mailbox.')


class LogoutTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_logout_works(self):
        """
        Check that logout works
        """
        self.client.post(reverse('register'), {
                         'email': 'f@f', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse("logout"), follow=True)
        self.assertEquals(response.context['user'].username, '')


class EmailRetrievalTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_invalid_id_sends_error(self):
        """
        An invalid ID should send an error
        """
        self.client.post(reverse('register'), {
                         'email': 'a@a', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(
            reverse('mail:email', kwargs={'email_id': 1000}))
        self.assertEquals(json.loads(response.content)[
                          'error'], 'Email not found.')

    def test_post_request_sends_error(self):
        """
        POST request to the API should give an error
        """
        self.client.post(reverse('register'), {
                         'email': 'a@a', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse('mail:home'))
        user3 = User.objects.get(username=response.context['user'].username)

        email = Email(
            user=user3,
            sender=user3,
            subject="Test",
            body="Test",
            read=False,
        )
        email.save()
        email.recipients.add(user3)
        email.save()
        response = self.client.post(
            reverse('mail:email', kwargs={'email_id': 1}))
        self.assertEquals(json.loads(response.content)[
                          'error'], 'GET or PUT request required.')

    def test_valid_request_returns_correct_email(self):
        """
        POST request to the API should
         give an error
        """
        self.client.post(reverse('register'), {
                         'email': 'a@a', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse('mail:home'))
        user3 = User.objects.get(username=response.context['user'].username)

        email = Email(
            user=user3,
            sender=user3,
            subject="Test",
            body="Test",
            read=False,
        )
        email.save()
        email.recipients.add(user3)
        email.save()
        response = self.client.get(
            reverse('mail:email', kwargs={'email_id': 1}))
        self.assertEqual(json.loads(response.content), email.serialize())

    def test_put_request_work(self):
        """
        put request to the API should change the email
        """
        self.client.post(reverse('register'), {
                         'email': 'a@a', 'password': 'abc',
                         'confirmation': 'abc'})
        response = self.client.get(reverse('mail:home'))
        user3 = User.objects.get(username=response.context['user'].username)

        email = Email(
            user=user3,
            sender=user3,
            subject="Test",
            body="Test",
            read=False,
        )
        email.save()
        email.recipients.add(user3)
        email.save()
        self.client.put(reverse('mail:email', kwargs={'email_id': 1}),
                        json.dumps(
            {"read": True, "archived": True}), content_type='application/json')
        response = self.client.get(
            reverse('mail:email', kwargs={'email_id': 1}))
        self.assertTrue(json.loads(response.content)['archived'])
        self.assertTrue(json.loads(response.content)['read'])


class LoginPageTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_login_works(self):
        """
        Login with correct credential should work
        """
        self.client.post(reverse('register'), {
                         'email': 'a@a', 'password': 'abc',
                         'confirmation': 'abc'})
        self.client.logout()

        self.client.post(reverse('login'), {'email': 'a@a',
                                            'password': 'abc'})
        response = self.client.get(reverse('mail:home'))
        self.assertEquals(response.context['user'].username, 'a@a')

    def test_login_with_wrong_ceredentials_fails(self):
        """
        Login with wrong credential should fail
        """
        self.client.post(reverse('register'), {
                         'email': 'a@a', 'password': 'abc',
                         'confirmation': 'abc'})
        self.client.logout()

        self.client.post(reverse('login'), {
                         'email': 'a@a', 'password': 'helloimahacker'})
        response = self.client.get(reverse('mail:home'), follow=True)
        self.assertEquals(response.context['user'].username, '')
