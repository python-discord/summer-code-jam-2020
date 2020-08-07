from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = "/accounts/login/"
