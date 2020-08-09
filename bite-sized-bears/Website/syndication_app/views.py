import imghdr
from functools import update_wrapper

from django.views import View as ParentView
from django.db.models import Count
from django.views.generic import ListView
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import classonlymethod
from django.contrib.auth.models import User as AuthUser

from .models import Post, Comments, User, Community


class View(ParentView):
    """
    Custom View Class for extending the django User Model
    """
    @classonlymethod
    def as_view(cls, **initkwargs):
        for key in initkwargs:
            if key in cls.http_method_names:
                raise TypeError("You tried to pass in the %s method name as a "
                                "keyword argument to %s(). Don't do that."
                                % (key, cls.__name__))
            if not hasattr(cls, key):
                raise TypeError("%s() received an invalid keyword %r. as_view "
                                "only accepts arguments that are already "
                                "attributes of the class." % (cls.__name__, key))

        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            try:
                request.user = User.objects.get(name=request.user.get_username())
                auth_user = AuthUser.objects.get(username=request.user.name)
                for meth in dir(auth_user):
                    if not hasattr(request.user, meth):
                        try:
                            setattr(request.user, meth, getattr(auth_user, meth))
                        except Exception:
                            pass
            except Exception:
                pass
            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get
            self.setup(request, *args, **kwargs)
            if not hasattr(self, 'request'):
                raise AttributeError(
                    "%s instance has no 'request' attribute. Did you override "
                    "setup() and forget to call super()?" % cls.__name__
                )
            return self.dispatch(request, *args, **kwargs)

        view.view_class = cls
        view.view_initkwargs = initkwargs

        update_wrapper(view, cls, updated=())

        update_wrapper(view, cls.dispatch, assigned=())
        return view


class IndexListView(ListView, View):
    paginate_by = 25
    template_name = 'index.html'
    queryset = Post.objects.all()


class MostViewedPost(ListView, View):
    template_name = 'most-viewed.html'
    paginate_by = 15
    queryset = Post.objects.annotate(
        v_count=Count('views')
    ).order_by('-v_count')


class CommunityListView(ListView, View):
    template_name = 'top-community.html'
    paginate_by = 20
    queryset = Community.objects.all().annotate(
        s_count=Count('subscribers')
    ).order_by('-s_count')[:100]


class MyCommunityListView(ListView, View):
    template_name = 'my-communities.html'
    paginate_by = 15

    def get_queryset(self):
        queryset = \
            Community.objects.filter(subscribers__name=self.request.user.get_username())
        return queryset


class PostView(View):
    template_name = 'single-post.html'
    model = Post
    context = {}

    def get(self, request, community_name, post_id): # noqa
        post = self.model.objects.get(id=post_id)
        if request.user.is_authenticated:
            user = User.objects.get(name=request.user.get_username())
            if user not in post.views.all():
                post.views.add(user)
        comments = post.comment_post.all()
        self.context = {"comments": comments, "post": post}
        return render(request, self.template_name, self.context)


class SignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        try:
            return render(request, self.template_name, {'next': request.POST['next']})
        except Exception:
            return render(request, self.template_name, {'next': False})

    def post(self, request):
        try:
            username = request.POST["username"]
        except Exception:
            to_render = self.get(request)
            return to_render
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(name=username).exists():
                message = "Username is already taken"
                created = False
            else:
                user = User(name=username, password=password1)
                user.save()
                user = auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                message = "Account created successfully"
                created = True
        else:
            created = False
            message = "Passwords does not match. Try again."

        try:
            next = request.POST['next']
            if created:
                return redirect(next)
        except Exception:
            pass
        try:
            return render(request, self.template_name, {"message": message, "created": created, 'next': next})
        except Exception:
            return render(request, self.template_name, {"message": message, "created": created, 'next': False})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        try:
            return render(request, self.template_name, {"created": True, 'next': request.POST['next']})
        except Exception:
            return render(request, self.template_name, {"created": True, 'next': False})

    def post(self, request):
        try:
            username = request.POST["username"]
        except Exception:
            to_render = self.get(request)
            return to_render
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        try:
            next = request.POST['next']
        except Exception:
            pass
        if user is not None:
            auth.login(request, user)
            try:
                return redirect(next)
            except Exception:
                return redirect('/')
        else:
            try:
                return render(
                    request,
                    self.template_name, {"message": "Account does not exist",
                                         "created": False,
                                         'next': next
                                         }
                )
            except Exception:
                return render(
                    request,
                    self.template_name, {"message": "Account does not exist",
                                         "created": False,
                                         'next': False
                                         }
                )


class CommunityView(View):
    template_name = 'community.html'
    model = Community
    context = {}

    def get(self, request, community_name):
        community = self.model.objects.get(name=community_name)
        post = community.post_publisher.all()
        context = {"community": community, "posts": post}
        if community.subscribers.filter(name=request.user.get_username()):
            context["subscribed"] = True
        return render(request, self.template_name, context)


class UserView(View):
    template_name = 'user-posts.html'
    model = User
    context = {}

    def get(self, request, username):
        self.context['user_data'] = self.model.objects.get(name=username)
        self.context['posts'] = self.context['user_data'].post_author.all() \
            .annotate(v_count=Count('views')).order_by('-v_count')
        return render(request, self.template_name, self.context)


class UserProfileUpdate(UpdateView, View):
    model = User
    fields = ['avatar']
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        try:
            if imghdr.what(form.instance.avatar) and imghdr.what(form.instance.avatar) != 'gif':
                return super().form_valid(form)
        except Exception:
            pass
        ctx = self.get_context_data(form=form)
        ctx['message'] = 'Invalid picture'
        return self.render_to_response(ctx)

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        user = context.pop('user')
        context['user_data'] = user
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )


class store_args:
    pass


class PostCreate(CreateView, View):
    model = Post
    fields = ['title', 'description']
    template_name_suffix = '_create_form'
    valves = store_args()

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(request.META['HTTP_REFERER'])
        for val in args:
            setattr(self.valves, val, val)
        for key, val in kwargs.items():
            setattr(self.valves, key, val)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.publisher = Community.objects.get(name=self.valves.community_name)
        return super().form_valid(form)


class CommunityCreate(CreateView, View):
    model = Community
    fields = ['name', 'description', 'location']
    template_name_suffix = '_create_form'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(request.META['HTTP_REFERER'])
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class HomeListView(ListView, View):

    template_name = 'index.html'
    paginate_by = 25

    def get_queryset(self):
        queryset = \
            Post.objects.filter(
                publisher__in=Community.objects.prefetch_related('subscribers')
                .filter(subscribers__name__exact=self.request.user.get_username()
                        )).annotate(post_views=Count('views')).order_by('-post_views')
        return queryset


@login_required
def subscription_request(request, community_name):
    username = request.user.get_username()
    community = Community.objects.get(name=community_name)
    user = User.objects.get(name=username)
    if user in community.subscribers.all():
        community.subscribers.remove(user)
    else:
        community.subscribers.add(user)

    return redirect(request.META['HTTP_REFERER'])


def add_comment(request, community_name, post_id):
    author = User.objects.get(name=request.user.get_username())
    post = Post.objects.get(id=post_id)
    content = request.POST['content']
    Comments.objects.create(content=content, author=author, post=post)

    return redirect(f'/community/{community_name}/{post_id}')


def logout_request(request):
    auth.logout(request)
    return redirect('/')
