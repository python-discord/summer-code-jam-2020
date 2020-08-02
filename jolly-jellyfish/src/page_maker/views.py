from django.views.generic import (
    TemplateView,
    FormView
)

from .forms import UserRegisterForm


class MainView(TemplateView):
    template_name = "page_maker/main.html"


class UserRegister(FormView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = '/users/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
