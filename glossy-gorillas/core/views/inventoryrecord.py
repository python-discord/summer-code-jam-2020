from django.contrib.auth.mixins import LoginRequiredMixin
from core import models
from django.views.generic import CreateView


class InventoryAdditionForm(LoginRequiredMixin, CreateView):
    model = models.InventoryRecord
    template_name = "core/inventory_form.html"
    success_url = "../dashboard"
    fields = ["product", "quantity", "quantity_type"]

    def form_valid(self, form):
        form.instance.owner = self.request.user.trader
        return super().form_valid(form)
