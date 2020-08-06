from django.views.generic.list import ListView
from core.models.market import Listing


class HomeView(ListView):
    model = Listing
    template_name = "core/pages/home.html"
    context_object_name = "listings"

    def get_queryset(self):
        return Listing.objects.newest_10()
