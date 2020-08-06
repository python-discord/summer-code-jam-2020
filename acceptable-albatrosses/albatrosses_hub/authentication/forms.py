from django import forms


class RegisterForm(forms.Form):
    """ This class contains all required forms for regsitration. """

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
