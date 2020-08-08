from django import forms


class RegisterForm(forms.Form):
    """This class contains all required forms for registration."""

    email = forms.EmailField(
        label="Your Email",
    )
    username = forms.CharField(
        label="Your Username",
        max_length=32,
    )
    password = forms.CharField(
        label="Enter Your Password",
        max_length=64,
        widget=forms.PasswordInput(),
    )
    re_password = forms.CharField(
        label="Re-enter Your Password",
        max_length=64,
        widget=forms.PasswordInput(),
    )


class LoginForm(forms.Form):
    """This class contains all required forms for login."""

    email = forms.EmailField(
        label="Your Email",
    )
    password = forms.CharField(
        label="Enter Your Password",
        max_length=64,
        widget=forms.PasswordInput(),
    )
