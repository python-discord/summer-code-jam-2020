from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import UserProfile

import pycountry



from .forms import MySiteUserCreationForm


class SignUpView(CreateView):
    form_class = MySiteUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def home(request):
    return render(request, 'users/home.html')


def user(request, user_id):
    try:
        user_prof_obj = UserProfile.objects.get(id=user_id)
        return render(request, 'users/user.html', {'user_prof': {'username': user_prof_obj.username,
                                                                 'email': user_prof_obj.email,
                                                                 'image': user_prof_obj.image,
                                                                 'gender': {'M': 'Male', 'F': 'Female', 'D': 'Other'}[user_prof_obj.gender],
                                                                 'country': pycountry.countries.get(alpha_2=user_prof_obj.country).name,
                                                                 'city': user_prof_obj.city,
                                                                 'date_of_birth': user_prof_obj.date_of_birth},
                                                   'title': user_prof_obj})
    except UserProfile.DoesNotExist:
        # PyCharm flags this as Unknown Attribute Reference but it still does what it's supposed to
        return redirect('users-home')
