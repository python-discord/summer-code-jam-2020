# from django.conf import settings
from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.models import User
from anon.models import AnonUser
from anon.views import random_string
import datetime


class AnonBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        id = request.session.get("ID")
        if not id:
            user = AnonUser.objects.create(last_seen=datetime.datetime.now(), auth_token=random_string(30))
            request.session['ID'] = user.id
        else:
            user = AnonUser.objects.get(id=id)

        # try:
        #     user = User.objects.get(id=username)
        #     if user:
        #         return user
        # except User.DoesNotExist:
        #     return User().set_password(password)

        return user
