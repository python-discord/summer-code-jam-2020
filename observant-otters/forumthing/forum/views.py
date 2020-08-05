from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Thread, Message


def home(request):
    return render(request, 'forum/home.html', {})


class NewThread(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewMessage(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # set the author to user
        thread_path = self.request.path.replace('/new', '')  # parse which thread this was posted in
        form.instance.thread = Thread.objects.filter(pk=int(thread_path[thread_path.rfind('/') + 1:])).first()
        return super().form_valid(form)


def threads(request, t_id=None):
    if request.method == "GET":
        return _threads_no_auth(request, t_id)
    else:
        return _threads_auth(request, t_id)


# Handles just the GETs
def _threads_no_auth(request, t_id=None):
    if t_id is None:
        return render(request, 'forum/home.html')

    t_id = int(t_id)
    next_page = Thread.objects.filter(pk__gt=t_id).first()  # note: gt means greater than
    next_exists = bool(next_page)
    prev_page = Thread.objects.filter(pk__lt=t_id).last()  # and lt means less than
    prev_exists = bool(prev_page)

    thread = get_object_or_404(Thread, id=int(t_id))  # don't want them to get a thread that doesn't exist now
    p = int(request.GET.get("p", default=1))
    data = {
        "thread": thread,
        "messages": thread.message_set.all(),
        "id": t_id,
        "page": p,

        # @TODO: Remove debug values
        "next_page": p + 1,
    }

    if p > 1:
        data.update({"prev_page": p - 1})
    if prev_exists:
        data.update({"prev_id": prev_page.pk})
    if next_exists:
        data.update({"next_id": next_page.pk})

    return render(request, 'forum/thread.html', data)


@login_required
def _threads_auth(request, t_id=None):
    if request.method == "POST":
        _handle_post(request, t_id=t_id)
    elif request.method == "DELETE":
        _handle_delete(request, t_id)
    elif request.method == "PATCH":
        _handle_patch(request, t_id)


def _handle_post(request, t_id=None):
    if t_id is None:
        pass  # @TODO: Handle new thread creation
    else:
        pass  # @TODO: Handle new thread reply creation


def _handle_delete(request, t_id):
    pass  # @TODO: Handle thread deletion


def _handle_patch(request, t_id):
    pass  # @TODO: Handle thread edit
