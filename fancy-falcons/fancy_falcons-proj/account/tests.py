from django.test import TestCase
from django.db.models import Count
from .models import Account

class AccountModelTests(TestCase):
    def setUp(self):
        Account.objects.create(first_name="Bob", last_name="Hope", earldom="York", email="test1@test.test")
        Account.objects.create(first_name="John", last_name="Wick", earldom="York", email="test2@test.test")
        Account.objects.create(first_name="Bob", last_name="Seger", earldom="Sussex", email="test3@test.test", title="King")

    def test_all_accounts_hold_earl_title(self):
        """
        All accounts need have to have Earl title
        """
        accounts = Account.objects.all()
        earls = Account.objects.filter(title='Earl')
        self.assertEquals(accounts, earls)

    def test_no_duplicate_earldoms(self):
        """
        There can only be one Earl per Earldom
        """
        dupes = Account.objects.values('earldom').annotate(count=Count('id')).values('earldom').order_by().filter(count__gt=1)
        self.assertFalse(dupes)