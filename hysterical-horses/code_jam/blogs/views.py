from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.views.generic.list import ListView
from users.mixins import LevelRestrictionMixin

from .filters import PostFilter
from .forms import CommentForm
from .models import Comment, Post


@login_required
def like_view(request, pk):
    """
    If user already liked the post, remove their like.
    If the user has not already liked the post, add their like.
    """
    post = get_object_or_404(Post, id=request.POST.get("post_id"))

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse("blog_detail", args=[str(pk)]))


class HomeView(LoginRequiredMixin, LevelRestrictionMixin, ListView):
    model = Post
    template_name = "blogs_list.html"

    filterset_class = PostFilter

    def test_func(self):
        return self.request.user.blogs_unlocked

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filterset"] = self.filterset
        return context


class BlogDetailView(LoginRequiredMixin, LevelRestrictionMixin, DetailView):
    model = Post
    template_name = "blog_detail.html"

    def test_func(self):
        return self.request.user.blogs_unlocked

    def get_parent_id(self):
        """
        If the comment is sent via the reply version of the comment form,
        the form will be sent with a hidden input that is named 'parent_id'
        and has the value of the head comment.
        """
        try:
            parent_id = int(self.request.POST.get("parent_id"))
        except Exception as e:
            print(e)
            parent_id = None

        return parent_id

    def post(self, request, *args, **kwargs):
        print("POST METHOD RUNNING")

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            self.object = self.get_object()  # Required for context data
            context = super(BlogDetailView, self).get_context_data(**kwargs)
            comment_post = context["post"]

            # If it is a reply comment, add parent_obj
            if parent_id := self.get_parent_id():
                new_comment = comment_form.save(commit=False)

                parent_obj = Comment.objects.get(id=parent_id)
                new_comment.parent = parent_obj

            new_comment = comment_form.save(commit=False)
            new_comment.post = comment_post
            new_comment.author = request.user
            new_comment.save()  # Save to database
            return HttpResponseRedirect(self.request.path_info)  # Refresh

    def get_context_data(self, **kwargs):
        """Runs when GET is called."""
        print("CONTEXT DATA RUNNING")

        context = super().get_context_data(**kwargs)
        blog_post = context["post"]

        # Comments
        comments = blog_post.comments.filter(
            active=True, parent__isnull=True
        )  # Non-reply comments only
        context["comments"] = comments

        # Comment form
        comment_form = CommentForm()
        context["comment_form"] = comment_form

        # Total likes
        context["total_likes"] = blog_post.total_likes

        # Has the user liked?
        liked = False
        if blog_post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["liked"] = liked

        return context


class PostCreateView(LoginRequiredMixin, LevelRestrictionMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def test_func(self):
        return self.request.user.blogs_posting_unlocked

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
