from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from core import models
from django.urls import reverse_lazy


class TraderDashboard(LoginRequiredMixin, DetailView):
    template_name = "core/dashboard.html"
    login_url = reverse_lazy("login")
    model = models.Trader

    def get_object(self, queryset=None):
        return self.request.user.trader

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["listings"] = (
            models.Listing.objects.filter(item__owner=self.object)
            .exclude(status=models.ListingStatus.FINALIZED)
            .values(
                "item__product__name",
                "item__quantity",
                "item__quantity_type",
                "silver_per_unit",
                "barter_product",
                "barter_qty_per_unit",
                "allow_offers",
            )
        )

        context["inventory"] = models.InventoryRecord.objects.filter(
            owner=self.object
        ).values("product__name", "quantity", "quantity_type",)

        context["reviews"] = models.Review.objects.filter(
            trade__listing__item__owner=self.object
        ).values("rating", "description",)

        return context