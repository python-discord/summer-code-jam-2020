from django.views.generic import DetailView, ListView
from .models import Rover
from posts.models import ImagePost


class RoverProfileView(DetailView):
    model = Rover
    template_name = "rovers/profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"

    # add the most recent 8 images that this rover has posted to the context
    def get_context_data(self, **kwargs):
        context = super(RoverProfileView, self).get_context_data(**kwargs)
        context["images"] = ImagePost.objects.filter(rover=context["rover"]).order_by(
            "-date"
        )[:8]
        return context


class RoverProfileListView(ListView):
    model = Rover
    template_name = "rovers/rovers.html"
    context_object_name = "rovers"
    ordering = ["username"]
