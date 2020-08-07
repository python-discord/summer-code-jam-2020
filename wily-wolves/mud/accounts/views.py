from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm

from game.models import Player


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)
        Player.objects.create(user=self.object)
        return response


class ProfileView(TemplateView):
    template_name = 'registration/profile.html'
