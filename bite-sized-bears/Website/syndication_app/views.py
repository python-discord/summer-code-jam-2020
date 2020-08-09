from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views import View
from .models import Post, Comments, User, Community
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required


class IndexListView(ListView):
    paginate_by = 25
    template_name = 'index.html'
    queryset = Post.objects.all()


class PostView(View):
    template_name = 'single-post.html'
    model = Post
    context = {}

    def get(self, request, community_name, post_id):
        post = self.model.objects.get(id=post_id)
        comments = post.comment_post.all()
        self.context = {"comments": comments, "post": post}
        return render(request, self.template_name, self.context)


class SignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(name=username).exists():
                messages.error(request, 'Oops, something bad happened')
                message = "Username is already taken"
                created = False
            else:
                user = User(name=username, password=password1)
                user.save()
                message = "Account created successfully"
                created = True
        else:
            created = False
            message = "Passwords does not match. Try again."

        return render(request, self.template_name, {"message": message, "created": created})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name, {"created": True})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(request.META['HTTP_REFERER'])
        else:
            return render(request, self.template_name, {"message": "Account does not exist", "created": False})


class CommunityView(View):
    template_name = 'community.html'
    model = Community

    def get(self, request, community_name):
        community = self.model.objects.get(name=community_name)
        post = community.post_publisher.all()
        context = {"community": community, "post": post}
        if community.subscribers.filter(name=request.user.get_username()):
            context["subscribed"] = True
        return render(request, self.template_name, context)


class UserView(View):
    template_name = 'user-posts.html'
    model = User
    context = {}

    def get(self, request, username):
        self.context['user'] = self.model.objects.get(name=username)
        self.context['posts'] = self.context['user'].post_author.all() \
            .annotate(v_count = Count('views')).order_by('-v_count')
        return render(request, self.template_name, self.context)


class CommunityListView(ListView):
    template_name = 'top-community.html'
    paginate_by = 25
    queryset = Community.objects.all().annotate(
        s_count=Count('subscribers')
    ).order_by('-s_count')[:100]


class UserProfileUpdate(UpdateView):
    model = User
    fields = ['avatar']
    template_name_suffix = '_update_form'


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
    community.subscribers.add(user)
    return redirect(request.META['HTTP_REFERER'])