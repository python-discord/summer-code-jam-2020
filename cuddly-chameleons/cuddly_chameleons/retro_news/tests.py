import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from retro_news.models import CustomUser

client = Client()


class CreateUserUnitTests(TestCase):
    """Contains tests about user signing up endpoint."""

    def test_create_valid_user(self):
        """Check does this create new user with valid payload."""
        response = client.post(
            reverse('create_user'),
            data=json.dumps({
                'email': 'test@test.com',
                'username': 'test',
                'password': 'myvalidpassword1234'
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        """Check does request fail with code 400 when invalid data provided."""
        # Create user for duplicate check
        CustomUser.objects.create(username="duplicate", email="unit@test.com", password="1234")

        invalid_datasets = [
            {
                'email': 'test@test.com',
                'username': 'duplicate',  # duplicate user
                'password': '1234567890',
            },
            {
                'email': 'test@test.com',
                'username': 'valid',
                'password': '1234',  # password too short
            },
            {
                'email': 'foobar',  # invalid email
                'username': 'valid2',
                'password': '1234567890',
            },
            {
                'email': '',  # empty email
                'username': 'valid3',
                'password': '1234567890',
            },
            {
                'email': 'test@test.com',
                'username': '',  # empty username
                'password': '1234567890',
            },
            {
                'email': 'test@test.com',
                'username': 'valid4',
                'password': '',  # empty password
            },
            {
                # All empty
                'email': '',
                'username': '',
                'password': '',
            },
        ]

        for dataset in invalid_datasets:
            response = client.post(
                reverse('create_user'),
                data=json.dumps(dataset),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
