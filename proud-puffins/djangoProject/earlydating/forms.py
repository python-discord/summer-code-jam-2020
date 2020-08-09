from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CreateUserForm(UserCreationForm):
    """Registration/Sign-up Form"""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """Form for editing information in User table fields"""
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """Form for editing information in Profile table fields"""
    class Meta:
        model = Profile
        fields = ['age', 'bio', 'img', 'sex', 'preference']
