from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from .models import PhoneNumber

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PhoneNumberForm(forms.ModelForm):
    phone_number = PhoneNumberField()

    class Meta:
        model = PhoneNumber
        fields = ['phone_number']
