from django.contrib.auth.models import User
from django.test import TestCase
import pytest
from mixer.backend.django import mixer
from dungeon.models.character import MudUser


##
#  If you try to do something, you will have to make a user.
##
# You can debug by inserting pyest.set_trace() into the middle of the code.
# The print does not work in the test. (Use pytest.set_trace())
#
# pytest.set_trace()
# #
# The test case shall always be a method starting with a test.
# #
#  def test_abc(self):
# #

@pytest.mark.django_db
class BaseTestCase(TestCase):
    # Generated without user return.
    def create_hello_world_muduser(self):
        user = MudUser.objects.create(username='Hello_World')
        return user

    def create_one_muduser(self):
        user = mixer.blend(MudUser)
        return user

    def create_three_muduser(self):
        user1 = mixer.blend(MudUser)
        user2 = mixer.blend(MudUser)
        user3 = mixer.blend(MudUser)
        return (user1, user2, user3)

    def create_many_muduser(self):
        for i in range(50):
            mixer.blend(MudUser)

    def create_hello_world_user(self):
        user = User.objects.create(username='Hello_World')
        return user

    def create_one_user(self):
        user = mixer.blend(User)
        return user

    def create_three_user(self):
        user1 = mixer.blend(User)
        user2 = mixer.blend(User)
        user3 = mixer.blend(User)
        return (user1, user2, user3)

    def create_many_user(self):
        for i in range(50):
            mixer.blend(User)
