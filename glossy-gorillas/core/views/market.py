from django.views.generic import ListView
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
