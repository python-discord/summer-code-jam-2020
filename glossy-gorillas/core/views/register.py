from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from core.forms import UserRegisterForm


class Register(FormView):
    """Creates user if valid. Otherwise, form must be repeated."""

    form_class = UserRegisterForm
    template_name = "core/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        messages.success(self.request, f"Account created for {username}!")
        return super().form_valid(form)
