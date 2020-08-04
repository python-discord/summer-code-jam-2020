from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import (
    LoginView,
)
from django.views.generic import (
    CreateView
)
from django.contrib.auth.forms import (
    UserCreationForm
)


class login_view(LoginView):
    template_name = 'login.html'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login-view')
    template_name = 'registration/create_user.html'


def logout_view(request):
    logout(request)
    return render(request, 'twentytwentymud/splash.html')


def index(request):
    return render(request, 'twentytwentymud/splash.html')
