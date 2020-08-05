from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ImagePost
from rovers.models import Rover


class ImagePostListView(ListView):
    model = ImagePost
    template_name = "posts/home.html"
    context_object_name = "posts"
    ordering = ["-date"]
    paginate_by = 16


class ImagePostDetailView(DetailView):
    model = ImagePost
    template_name = "posts/imagepost.html"

    # get URLs for the previous/next photos
    def get_context_data(self, **kwargs):
        # get the default context to append to
        context = super(ImagePostDetailView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username")
        try:
            # if viewing image from a profile, only navigate to that rover's images
            rover = Rover.objects.get(username=username)
            imageposts = list(ImagePost.objects.filter(rover=rover).order_by("-date"))
            username_get = "?username=" + username
        except:
            # if no valid username, navigate to next/prev image regardless of rover
            imageposts = list(ImagePost.objects.all().order_by("-date"))
            username_get = ""

        # if only one image returned, no links required
        prev_image_pk = next_image_pk = "#"
        if len(imageposts) > 1:
            displayed_image_index = imageposts.index(self.get_object())
            if displayed_image_index == 0:
                prev_image_pk = imageposts[-1].pk
            else:
                prev_image_pk = imageposts[displayed_image_index - 1].pk
            if displayed_image_index == len(imageposts) - 1:
                next_image_pk = imageposts[0].pk
            else:
                next_image_pk = imageposts[displayed_image_index + 1].pk
        else:
            # username_get is not needed if only one post
            username_get = ""

        # add links to context for template to use
        context["prev_image_pk"] = prev_image_pk
        context["next_image_pk"] = next_image_pk
        context["username_get"] = username_get
        return context
