from django.views.generic.list import ListView
from core.models.market import Listing, Trade


class HomeView(ListView):
    model = Listing
    template_name = "core/pages/home.html"
    context_object_name = "listings"

    def get_queryset(self):
        return Listing.objects.newest_10()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['trades'] = Trade.objects.newest_10()
        return context
