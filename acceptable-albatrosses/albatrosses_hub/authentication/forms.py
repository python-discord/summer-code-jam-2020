from django import forms


class RegisterForm(forms.Form):
    """This class contains all required forms for registration."""

    email = forms.EmailField(label="Your Email",)
    username = forms.CharField(label="Your Username", max_length=30,)
    password = forms.CharField(label="Enter Your Password", max_length=64, widget=forms.PasswordInput(),)
    re_password = forms.CharField(label="Re-enter Your Password", max_length=64, widget=forms.PasswordInput(),)


class LoginForm(forms.Form):
    """This class contains all required forms for login."""

    username = forms.CharField(label="Your Username", max_length=30)
    password = forms.CharField(label="Enter Your Password", max_length=64, widget=forms.PasswordInput(),)
