from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # required=True is default
    email = forms.EmailField(required=True)

    # whenever the form validates, it will create a new User
    # the model that will be affected is the User model
    class Meta:
        model = User
        # order in which fields should be displayed
        fields = ['username', 'email', 'password1', 'password2']
