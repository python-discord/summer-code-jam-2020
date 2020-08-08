from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = [
            'email',
            'first_name',
            'last_name',
            'passport_id',
            'password1',
            'password2',
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'email',
            'image',
        ]

