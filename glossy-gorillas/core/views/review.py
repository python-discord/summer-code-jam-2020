from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from core import models


class ReviewCreate(LoginRequiredMixin, CreateView):
    model = models.Review
    fields = ["trade", "rating", "description"]
    template_name = "core/review_create_form.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
