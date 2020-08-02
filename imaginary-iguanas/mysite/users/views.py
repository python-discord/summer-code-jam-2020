from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import MySiteUserCreationForm


class SignUpView(CreateView):
    form_class = MySiteUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def user(request, user_id):
    # user_obj = User.objects.get(pk=user_id)
    # return render(request, 'user/user.html', {'user': user_obj})
    return render(request, 'users/user.html')
