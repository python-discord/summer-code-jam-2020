from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile


class MySiteUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = UserProfile
        fields = (
            'username',
            'email',
            'gender',
            'country',
            'city',
            'date_of_birth')  # It needs to be formatted exactly this way, otherwise an Exception will be thrown



