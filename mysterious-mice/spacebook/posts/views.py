from django.views.generic import ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist
from .models import ImagePost
from rovers.models import Rover


class ImagePostListView(ListView):
    """
    Provides a list of ImagePosts to be displayed in a grid. If a valid username is provided as a
    GET parameter, then the ImagePosts returned will be limited to that user. This parameter will
    be passed automatically if this page is navigated to from a rover's profile.
    """

    model = ImagePost
    template_name = "posts/home.html"
    context_object_name = "posts"
    ordering = ["-date"]
    paginate_by = 16

    # if a valid username provided, only return that rover's posts
    def get_queryset(self):
        username = self.request.GET.get("username")
        try:
            rover = Rover.objects.get(username=username)
            imageposts = ImagePost.objects.filter(rover=rover).order_by("-date")
        except ObjectDoesNotExist:
            imageposts = ImagePost.objects.all().order_by("-date")
        return imageposts

    # pass additional context if only displaying posts from one rover
    def get_context_data(self, **kwargs):
        # get the default context to append to
        context = super(ImagePostListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username")
        try:
            # if viewing posts by a specific rover, pass additional context to
            # add GET data to URL and to display username in header
            rover = Rover.objects.get(username=username)
            context["username_get"] = f"username={ rover.username }&"
            context["username"] = username
        except ObjectDoesNotExist:
            context["username_get"] = ""
        return context


class ImagePostDetailView(DetailView):
    """
    Provides a detail view for an ImagePost. If a valid username is provided as a GET parameter,
    the next and previous links will navigate through only that rover's ImagePosts. Otherwise they
    will navigate through all the ImagePosts on the site. This parameter will be passed
    automatically if this page is navigated to from a rover's profile.
    """

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
            username_get = f"?username={username}"
            context["username"] = username
        except ObjectDoesNotExist:
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
