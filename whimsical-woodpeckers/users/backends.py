from django.conf import settings
from django.contrib.auth.models import User

class EmailAuthBackend(ModelBackend):    
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user:
                return user
        except User.DoesNotExist:
            return User().set_password(password)