from django.contrib.auth.mixins import LoginRequiredMixin
from core import models
from django.views.generic import CreateView

class InventoryAdditionForm(LoginRequiredMixin,CreateView):
    model = models.InventoryRecord
    fields = ["Product","Quantity","Quantity Type"]

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)