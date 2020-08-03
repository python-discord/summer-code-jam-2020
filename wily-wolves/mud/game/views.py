# from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'game/register.html'
