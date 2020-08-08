from django.contrib.auth.mixins import LoginRequiredMixin
from core import models
from django.views.generic import CreateView


class InventoryAdditionForm(LoginRequiredMixin, CreateView):
    model = models.InventoryRecord
    template_name = "core/inventory_form.html"
    fields = ["product", "quantity", "quantity_type"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
