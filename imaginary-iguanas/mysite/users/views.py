from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import UserProfile

from .forms import MySiteUserCreationForm


class SignUpView(CreateView):
    form_class = MySiteUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def home(request):
    return render(request, 'users/home.html')


def user(request, user_id):
    try:
        user_prof = UserProfile.objects.get(id=user_id)
        return render(request, 'users/user.html', {'user_obj': user_prof, 'title': user_prof.username})
    except UserProfile.DoesNotExist:
        # PyCharm flags this as Unknown Attribute Reference but it still does what it's supposed to
        return redirect('users-home')

