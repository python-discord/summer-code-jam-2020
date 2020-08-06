from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class SignupView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/signup.html"
