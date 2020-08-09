from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .models import Board, Post, Comment


# Create your views here.
def forumspage(request):
    """
    Forums home page, displays all message boards, with information
    such as the total number of posts in each board.
    """
    context = {"boards": Board.objects.all(), "login": request.user.is_authenticated, "page": "forum"}
    return render(request, "forums/forum.html", context)


class PostListView(ListView):
    """
    Main page for the message board, displays all posts in the message
    board.
    """

    model = Post
    paginate_by = 5
    template_name = "forums/board.html"
    context_object_name = "posts"

    def get_queryset(self):
        """
        Queries and return all posts from the same message board.
        """
        self.board = get_object_or_404(Board, name=self.kwargs["board"])
        return Post.objects.filter(board=self.board, comment__isnull=True).order_by("-created_at")

    def get_context_data(self, **kwargs):
        """
        Adds board information into context (might not need this).
        """
        context = super().get_context_data(**kwargs)
        context['board'] = self.board
        context["login"] = self.request.user.is_authenticated
        context["page"] = "forum"

        return context


class PostDetailView(DetailView):
    """
    View of a single post and all the comments on the posts.
    """

    model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        """
        Adds all comments of post into context data.
        """
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            post=context['post']).order_by('-created_at')
        context["login"] = self.request.user.is_authenticated
        context["page"] = "forum"

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View of page when creating posts.
    """

    model = Post
    fields = ["subject", "message"]

    def form_valid(self, form):
        """
        Fills in fields not queried from user.
        """
        form.instance.created_by = self.request.user
        form.instance.board_id = get_object_or_404(Board, name=self.kwargs["board"]).id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Get context from logged in user status and current page.
        """
        context = super().get_context_data(**kwargs)
        context["login"] = self.request.user.is_authenticated
        context["page"] = "forum"

        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View of page when editing posts.
    """

    model = Post
    fields = ["subject", "message"]

    def test_func(self):
        """
        To check user has permission (user is created_by) to edit post.
        """
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False

    def form_valid(self, form):
        """
        Fills in fields not queried from user.
        """
        form.instance.updated_by = self.request.user
        form.instance.updated_at = timezone.now()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Get context from logged in user status and current page.
        """
        context = super().get_context_data(**kwargs)
        context["login"] = self.request.user.is_authenticated
        context["page"] = "forum"

        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View of page when deleting posts.
    """

    model = Post

    def get_success_url(self):
        """
        Generate correct url (the message board) after deleting posts.
        """
        return reverse("forums:board-view", kwargs={"board": self.kwargs["board"]})

    def test_func(self):
        """
        To check user has permission (user is created_by) to edit post.
        """
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False

    def get_context_data(self, **kwargs):
        """
        Get context from logged in user status and current page.
        """
        context = super().get_context_data(**kwargs)
        context["login"] = self.request.user.is_authenticated
        context["page"] = "forum"

        return context


class UserPostListView(ListView):
    """
    View of all posts and comments from a particular user.
    TBC: make comments have reference to post it comes from.
    """

    model = Post
    paginate_by = 5
    template_name = "forums/user_posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        """
        Queries and returns all posts from users.
        """
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(created_by=user).order_by("-created_at")

    def get_context_data(self, **kwargs):
        """
        Get context from logged in user status and current page.
        """
        context = super().get_context_data(**kwargs)
        context["login"] = self.request.user.is_authenticated
        context["page"] = "forum"

        return context


class CommentDetailView(DetailView):
    """
    View of particular comment (not useful in most cases).
    """

    model = Comment

    def get_context_data(self, **kwargs):
        """
        Get context from logged in user status and current page.
        """
        context = super().get_context_data(**kwargs)
        context["login"] = self.request.user.is_authenticated
        context["page"] = "forum"

        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    """
    View of page when creating comments.
    TBC: make this in-line.
    """

    model = Comment
    fields = ["message"]

    def form_valid(self, form):
        """
        Fills in fields not queried from user.
        """
        form.instance.created_by = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.board_id = get_object_or_404(Board, name=self.kwargs["board"]).id
        return super().form_valid(form)

    def get_success_url(self):
        """
        Generate correct url (the post) after deleting posts.
        """
        return reverse("forums:board-detail", kwargs={"board": self.kwargs["board"], "pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        """
        Get context from logged in user status and current page.
        """
        context = super().get_context_data(**kwargs)
        context["login"] = self.request.user.is_authenticated
        context["page"] = "forum"

        return context


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View when updating comments.
    """

    model = Comment
    fields = ["message"]

    def test_func(self):
        """
        Validates user created the comment.
        """
        comment = self.get_object()
        if self.request.user == comment.created_by:
            return True
        return False

    def form_valid(self, form):
        """
        Fills in fields not queried from user.
        """
        form.instance.updated_by = self.request.user
        form.instance.updated_at = timezone.now()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Get context from logged in user status and current page.
        """
        context = super().get_context_data(**kwargs)
        context["login"] = self.request.user.is_authenticated
        context["page"] = "forum"

        return context


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View when deleting comments.
    """

    model = Comment

    def get_success_url(self):
        """
        Generate correct url (the post) after deleting posts.
        """
        return reverse("forums:board-detail", kwargs={"board": self.kwargs["board"], "pk": self.kwargs["post_pk"]})

    def test_func(self):
        """
        Validates user created the comment.
        """
        comment = self.get_object()
        if self.request.user == comment.created_by:
            return True
        return False

    def get_context_data(self, **kwargs):
        """
        Get context from logged in user status and current page.
        """
        context = super().get_context_data(**kwargs)
        context["login"] = self.request.user.is_authenticated
        context["page"] = "forum"

        return context


class BoardCreateView(LoginRequiredMixin, CreateView):
    """
    View of page when creating posts.
    """

    model = Board
    fields = ["name", "description"]

    def get_success_url(self):
        return reverse("forums:home")

    def get_context_data(self, **kwargs):
        """
        Get context from logged in user status and current page.
        """
        context = super().get_context_data(**kwargs)
        context["login"] = self.request.user.is_authenticated
        context["page"] = "forum"

        return context
