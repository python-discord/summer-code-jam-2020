from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView, 
)


class login_view(LoginView):
    template_name = 'login.html'


def index(request):
    return render(request, 'twentytwentymud/splash.html')
