from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ForumUser


class ForumUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = ForumUser
        fields = ('username', 'nickname', 'email', 'password1', 'password2')


class ForumUserChangeForm(UserChangeForm):

    class Meta:
        model = ForumUser
        fields = ('nickname', 'email')  # username is permanent, but you can change your nickname
