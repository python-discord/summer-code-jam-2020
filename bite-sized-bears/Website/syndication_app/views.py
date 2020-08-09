from django.views import View as views
from django.db.models import Count
from django.views.generic import ListView
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import classonlymethod
from functools import update_wrapper
from django.contrib.auth.models import User as AuthUser

from .models import Post, Comments, User, Community


class View(views):
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
                        except Exception as e:
                            pass
            except:
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

        # take name and docstring from class
        update_wrapper(view, cls, updated = ())

        # and possible attributes set by decorators
        # like csrf_exempt from dispatch
        update_wrapper(view, cls.dispatch, assigned = ())
        return view


class IndexListView(ListView, View):
    paginate_by = 25
    template_name = 'index.html'
    queryset = Post.objects.all()


class PostView(View):
    template_name = 'single-post.html'
    model = Post
    context = {}

    def get(self, request, community_name, post_id):
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
        except:
            return render(request, self.template_name, {'next': False})

    def post(self, request):
        try:
            username = request.POST["username"]
        except:
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
        except:
            pass
        try:
            return render(request, self.template_name, {"message": message, "created": created, 'next': next})
        except:
            return render(request, self.template_name, {"message": message, "created": created, 'next': False})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        try:
            return render(request, self.template_name, {"created": True, 'next': request.POST['next']})
        except:
            return render(request, self.template_name, {"created": True, 'next': False})

    def post(self, request):
        try:
            username = request.POST["username"]
        except:
            to_render = self.get(request)
            return to_render
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        try:
            next = request.POST['next']
        except:
            pass
        if user is not None:
            auth.login(request, user)
            try:
                return redirect(next)
            except:
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
            except:
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


class MostViewedPost(ListView, View):
    template_name = 'most-viewed.html'
    paginate_by = 15
    queryset = Post.objects.annotate(v_count = Count('views')).order_by('-v_count')


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
        queryset = Community.objects.filter(subscribers__name=self.request.user.get_username())
        return queryset


class UserProfileUpdate(UpdateView, View):
    model = User
    fields = ['avatar']
    template_name_suffix = '_update_form'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        user=context.pop('user')
        context['user_data']=user
        return self.response_class(
            request = self.request,
            template = self.get_template_names(),
            context = context,
            using = self.template_engine,
            **response_kwargs
        )


def logout_request(request):
    auth.logout(request)
    return redirect('/')


def add_comment(request, community_name, post_id):
    author = User.objects.get(name=request.user.get_username())
    post = Post.objects.get(id = post_id)
    content = request.POST['content']
    Comments.objects.create(content = content, author = author, post = post)

    return redirect(f'/community/{community_name}/{post_id}')


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


class HomeListView(ListView, View):

    template_name = 'index.html'
    paginate_by = 25

    def get_queryset(self):
        queryset = Post.objects.filter(
            publisher__in=Community.objects.prefetch_related('subscribers')
                .filter(subscribers__name__exact=self.request.user.get_username())).annotate(post_views=Count('views')).order_by('-post_views')
        return queryset