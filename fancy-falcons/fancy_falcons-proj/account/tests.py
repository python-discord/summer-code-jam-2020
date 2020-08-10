from django.test import TestCase
from django.db.models import Count, Q
from .models import Account

class AccountModelTests(TestCase):
    def setUp(self):
        Account.objects.create(first_name="Bob", last_name="Hope", earldom="York", email="test1@test.test")
        Account.objects.create(first_name="John", last_name="Wick", earldom="York", email="test2@test.test", is_user=True)
        Account.objects.create(first_name="Bob", last_name="Seger", earldom="Sussex", email="test3@test.test", title="King", is_user=True)

    def test_all_user_accounts_hold_earl_title(self):
        """
        All user accounts need have to have Earl title
        """
        notEarls = Account.objects.filter(~Q(title='Earl')).filter(is_user=True)
        self.assertFalse(notEarls)

    def test_no_duplicate_earldoms(self):
        """
        There can only be one user Earl per Earldom
        """
        duplicateEarldoms = Account.objects.filter(is_user=True).values('earldom').annotate(count=Count('id')).values('earldom').order_by().filter(count__gt=1)
        self.assertFalse(duplicateEarldoms)