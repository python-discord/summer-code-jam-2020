from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class AnonBackend(ModelBackend):    
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(id=username)
            if user:
                return user
        except User.DoesNotExist:
            return User().set_password(password)