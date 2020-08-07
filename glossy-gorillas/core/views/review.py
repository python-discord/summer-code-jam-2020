from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from core import models


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = models.Review
    fields = ["trade", "rating", "description"]
    template_name = "core/review_create_form.html"
    success_url = "../dashboard"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
