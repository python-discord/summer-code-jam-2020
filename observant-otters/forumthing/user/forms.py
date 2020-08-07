from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ForumUser


class ForumUserCreationForm(UserCreationForm):

    class Meta:
        model = ForumUser
        fields = ('username', 'nickname', 'email')


class ForumUserChangeForm(UserChangeForm):

    class Meta:
        model = ForumUser
        fields = ('nickname', 'email', 'avatar')  # username is permanent, but you can change you email
