from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import reverse, redirect
from django.utils.translation import gettext as _
from core.forms import ListInventoryRecord
from core.models import Listing


class ListingList(ListView):
    """Display a listing result based on a search term

    TODO:
    - Handle 'search' query parameter to filter results
    - Add logical ordering
    - Handle additional filter query parameters
    """

    paginate_by = 25
    model = Listing
    template_name = "core/pages/listing_list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        if "search" in self.request.GET:
            term = self.request.GET.get("search")
            return qs.filter(item__product__name__icontains=term)
        else:
            return qs


class ListingCreate(LoginRequiredMixin, CreateView):
    model = Listing
    form_class = ListInventoryRecord
    template_name = "core/listing_create_form.html"
    success_url = reverse_lazy("dashboard")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"item_id": self.kwargs.get("item_id")})
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        user_records = self.request.user.trader.inventoryrecord_set.values_list(
            "id", flat=True
        )
        item_id = self.kwargs.get("item_id")
        if item_id not in user_records:
            messages.warning(
                self.request, _("The record you want to list does not exist")
            )
            return redirect(reverse("dashboard"))
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, _("Listing created!"))
        return super().form_valid(form)
