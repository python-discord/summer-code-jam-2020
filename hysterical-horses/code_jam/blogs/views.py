from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .filters import PostFilter
from .forms import CommentForm
from .models import Comment, Post


class HomeView(ListView):
    model = Post
    template_name = 'blogs_list.html'

    filterset_class = PostFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset
        )
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

    def post(self, request, *args, **kwargs):
        print("POST METHOD RUNNING")

        self.comment_form = CommentForm(request.POST)

        if self.comment_form.is_valid():
            parent_obj = None

            try:
                parent_id = int(self.request.POST.get('parent_id'))
            except Exception as e:
                print(e)
                parent_id = None

            self.object = self.get_object()
            context = super(BlogDetailView, self).get_context_data(**kwargs)
            comment_post = context['post']

            if parent_id is not None:
                parent_obj = Comment.objects.get(id=parent_id)

                if parent_obj:
                    reply_comment = self.comment_form.save(commit=False)
                    reply_comment.parent = parent_obj

            self.new_comment = self.comment_form.save(commit=False)
            print(args)
            self.new_comment.post = comment_post  #  Problem here
            # `comment_post` can only exist in `get_context_data`
            self.new_comment.author = request.user
            self.new_comment.save()
            return HttpResponseRedirect(self.request.path_info)  # Refresh

    def get_context_data(self, **kwargs):
        print("CONTEXT DATA RUNNING")
        if self.request.method == 'GET':
            self.comment_form = CommentForm()

        context = super().get_context_data(**kwargs)

        comment_post = context['post']
        comments = comment_post.comments.filter(
            active=True, parent__isnull=True
        )
        context['comments'] = comments
        context['comment_form'] = self.comment_form
        return context
