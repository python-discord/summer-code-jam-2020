from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    TemplateView,
    FormView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
    ListView
)

from .models import User, Webpage, Template, Comment
from .forms import UserRegisterForm, WebpageForm, TemplateForm, CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        user = self.get_object()
        context['user_pages'] = Webpage.objects.filter(author=user)
        return context


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'page_maker/user_update.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = '/'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'page_maker/user_delete.html'
    success_url = '/'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False


class WebpageCreateView(LoginRequiredMixin, FormView):
    template_name = 'page_maker/webpage_create.html'
    form_class = WebpageForm
    # success_url = '/pages'

    # TODO validate and sanitize text and images
    # TODO create thumbnail
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
    Display webpage
    """
    model = Webpage
    template_name = 'page_maker/webpage_view.html'
    context_object_name = 'webpage'
    slug_field = 'name'
    slug_url_kwarg = 'pagename'



class WebpageDetailView(DetailView):
    """
    Display webpage details and comment section
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
        return context


class WebpageListView(ListView):
    """
    Display webpages ordered by vote number
    """
    model = Webpage
    template = 'page_maker/webpage_list.html'
    context_object_name = 'webpages'
    paginate_by = 10
    ordering = ['-votes']


class WebpageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Webpage
    tempalate_name = 'page_maker/webpage_update.html'

    def test_func(self):
        webpage = self.get_object()
        if webpage.author == self.request.user:
            return True
        return False

    def get_queryset(self):
        webpage_name = self.kwargs.get('pagename')
        return Webpage.objects.filter(name=webpage_name)


class WebpageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Webpage
    template_name = 'page_maker/webpage_delete.html'

    def test_func(self):
        webpage = self.get_object()
        if webpage.author == self.request.user or self.request.user.is_superuser:
            return True
        return False

    def get_queryset(self):
        webpage_name = self.kwargs.get('pagename')
        return Webpage.objects.filter(name=webpage_name)


class TemplateCreateView(LoginRequiredMixin, FormView):
    template_name = 'page_maker/template_create.html'
    form_class = TemplateForm
    success_url = '/'

    # TODO validate and sanitize style sheet
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class TemplateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Template
    template_name = 'page_maker/template_delete.html'

    def test_func(self):
        template = self.get_object()
        if template.author == self.request.user or self.request.user.is_superuser:
            return True
        return False


class CommentCreateView(LoginRequiredMixin, FormView):
    http_method_names = ['post'] # POST request only
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


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    http_method_names = ['post']
    model = Comment

    def test_func(self):
        comment = self.get_object()
        if comment.author == self.request.user or self.request.user.is_superuser:
            return True
        return False
