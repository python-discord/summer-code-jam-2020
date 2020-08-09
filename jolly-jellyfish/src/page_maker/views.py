from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    FormView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView
)

from .forms import UserRegisterForm, WebpageForm, TemplateForm, CommentForm
from .models import User, Webpage, Template, Comment, Like


class MainView(TemplateView):
    template_name = "page_maker/main.html"


class UserRegister(FormView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = '/users/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserDetailView(DetailView):
    model = User
    context_object_name = 'viewed_user'
    template_name = 'page_maker/user_detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        # the user's pages are sorted by the most recently edited (most recent first)
        context['user_pages'] = Webpage.objects.filter(author=user).order_by('-last_edit_date')
        return context


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'page_maker/user_update.html'
    fields = ['first_name', 'last_name', 'email']
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'username': self.get_object().username})


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'page_maker/user_delete.html'
    success_url = '/'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False


class WebpageCreateView(LoginRequiredMixin, FormView):
    template_name = 'page_maker/webpage_create.html'
    form_class = WebpageForm
    # TODO: some form of preview of the template selected using the thumbnails generated?

    # TODO create thumbnail here instead of in template.

    # NB: Django pre-sanitizes text input already - https://docs.djangoproject.com/en/dev/topics/security/
    def form_valid(self, form):
        self.form = form
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        pagename = self.form.cleaned_data['name']
        return reverse_lazy('webpage-view', kwargs={'pagename': pagename})


class WebpageView(DetailView):
    """
    Display user-created webpage itself (with links to User's page and comments, i.e. 'WebpageDetailView')
    """
    model = Webpage
    template_name = 'page_maker/webpage_view.html'
    context_object_name = 'webpage'
    slug_field = 'name'
    slug_url_kwarg = 'pagename'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        webpage = self.get_object()
        context['num_likes'] = webpage.like_set.all().count()
        return context


class WebpageDetailView(DetailView):
    """
    Display webpage details, like features and comment section
    """
    model = Webpage
    template_name = 'page_maker/webpage_detail.html'
    context_object_name = 'webpage'
    slug_field = 'name'
    slug_url_kwarg = 'pagename'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        webpage = self.get_object()
        context['comments'] = Comment.objects.filter(parent_page=webpage)
        context['comment_form'] = CommentForm()
        context['num_likes'] = webpage.like_set.all().count()
        return context

    def post(self, request, *args, **kwargs):
        """Like button logic"""
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        if request.user.is_authenticated:  # user is logged in
            if request.user == self.object.author:  # it's the user's own page
                context['like_response'] = "You can't like your own page!"
            else:
                like_obj, created = Like.objects.get_or_create(author=request.user, parent_page=self.object)
                if created:  # this is first time the user has liked the webpage
                    context['like_response'] = 'Thanks for the like!'
                else:
                    like_obj.delete()
                    context['like_response'] = "You've now unliked this page."
        else:
            context['like_response'] = 'Please login to leave a like.'

        context['num_likes'] = self.object.like_set.all().count()  # updates like count
        return self.render_to_response(context)


class WebpageListView(ListView):
    """
    Display webpages in order specified when .as_view() is called in urls.py
    """
    model = Webpage
    template = 'page_maker/webpage_list.html'
    context_object_name = 'webpages'
    paginate_by = 5
    ordering = None

    def get_queryset(self):
        """Return the webpages sorted by either number of likes or datetime created"""
        return Webpage.objects.annotate(like_count=Count('like')).order_by(self.ordering)


class WebpageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Webpage
    template_name = 'page_maker/webpage_update.html'
    slug_field = 'name'
    slug_url_kwarg = 'pagename'
    fields = ['name', 'template_used', 'user_title',
              'user_text_1', 'user_text_2', 'user_text_3',
              'user_image_1', 'user_image_2', 'user_image_3',
              ]

    def test_func(self):
        webpage = self.get_object()
        if webpage.author == self.request.user:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('webpage-view', kwargs={'pagename': self.kwargs['pagename']})


class WebpageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Webpage
    template_name = 'page_maker/webpage_delete.html'
    success_url = reverse_lazy('webpage-list-recent')
    slug_field = 'name'
    slug_url_kwarg = 'pagename'

    def test_func(self):
        webpage = self.get_object()
        if webpage.author == self.request.user or self.request.user.is_superuser:
            return True
        return False


class TemplateCreateView(LoginRequiredMixin, FormView):
    template_name = 'page_maker/template_create.html'
    form_class = TemplateForm

    def form_valid(self, form):
        self.form = form
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        templatename = self.form.cleaned_data['name']
        return reverse_lazy('template-view', kwargs={'templatename': templatename})


class TemplateView(DetailView):
    """
    Display template using example page
    """
    model = Template
    template_name = 'page_maker/example_page.html'
    context_object_name = 'template'
    slug_field = 'name'
    slug_url_kwarg = 'templatename'


class TemplateDetailView(DetailView):
    model = Template
    template_name = 'page_maker/template_detail.html'
    context_object_name = 'template'
    slug_field = 'name'
    slug_url_kwarg = 'templatename'


class TemplateListView(ListView):
    model = Template
    template_name = 'page_maker/template_list.html'
    context_object_name = 'templates'
    paginate_by = 10


class TemplateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Template
    template_name = 'page_maker/template_delete.html'
    success_url = '/'
    slug_field = 'name'
    slug_url_kwarg = 'templatename'
    success_url = '/'

    def test_func(self):
        template = self.get_object()
        if template.author == self.request.user or self.request.user.is_superuser:
            return True
        return False


class CommentCreateView(LoginRequiredMixin, FormView):
    http_method_names = ['post']
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        parent_page = get_object_or_404(Webpage, name=self.kwargs.get('pagename'))
        form.instance.parent_page = parent_page
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        pagename = self.kwargs.get('pagename')
        return reverse_lazy('webpage-detail', kwargs={'pagename': pagename})

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            raise PermissionDenied(self.get_permission_denied_message())
        # redirect to login with 'next' pointing to detail view
        return redirect_to_login(reverse_lazy(
            'webpage-detail', kwargs={'pagename': self.kwargs.get('pagename')}
        ), self.get_login_url(), self.get_redirect_field_name())


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    http_method_names = ['post']
    model = Comment

    def test_func(self):
        comment = self.get_object()
        if comment.author == self.request.user or self.request.user.is_superuser:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()  # save pagename for success url
        self.pagename = comment.parent_page.name
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('webpage-detail', kwargs={'pagename': self.pagename})
