from django.test import TestCase
from ..models import Account


class TestModels(TestCase):
    def setUp(self):
        self.account1_username = "Account 1"
        self.account1_email = "account1_email@email.com"
        self.account1_password = "th1sisagoodsecret$"
        self.account1 = Account.objects.create(
            email=self.account1_email,
            username=self.account1_username,
            password=self.account1_password,
        )

    def test_basic_user_info(self):
        self.assertEquals(self.account1.username, self.account1_username)
        self.assertEquals(self.account1.email, self.account1_email)

    def test_account_assigned_correct_permissions(self):
        self.assertEquals(self.account1.is_admin, False)
        self.assertEquals(self.account1.is_superuser, False)
        self.assertEquals(self.account1.is_staff, False)

    def test_account_assigned_defaults(self):
        self.assertEquals(self.account1.number_of_posts, 0)
        self.assertEquals(self.account1.number_of_likes, 0)
        self.assertEquals(self.account1.number_of_comments, 0)
        self.assertEquals(self.account1.number_of_messages, 0)
        self.assertEquals(self.account1.score, 0)
        self.assertEquals(self.account1.searches_made, 0)
        self.assertEquals(self.account1.points, 0)
