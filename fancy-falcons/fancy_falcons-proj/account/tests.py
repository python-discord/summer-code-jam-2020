from django.test import TestCase
from .models import Account

class QuestionModelTests(TestCase):

    def all_accounts_hold_earl_title(self):
        accounts = Account.objects.all()
        earls = Account.objects.get(title='Earl')
        self.assertIs(accounts == earls, True)

    def no_duplicate_earldoms(self):
        self.assertEquals(Account.objects.all().values('earldom').annotate(Count('earldom')).count(), 1)
