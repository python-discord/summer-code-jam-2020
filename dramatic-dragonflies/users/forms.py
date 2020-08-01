from django.contrib.auth.forms import UserCreationForm
import django.forms as forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        fields = ['username', 'email', 'password1', 'password2']
