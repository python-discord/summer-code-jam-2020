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
            'earldom',
            'password1',
            'password2',
        ]


class UserUpdateForm(forms.ModelForm):
    birthday = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateTimeInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'))

    class Meta:
        model = Account
        fields = [
            'first_name',
            'last_name',
            'earldom',
            'birthday',
            'email',
            'image',
        ]

