from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Thread, Message


class NewThread(CreateView):
    model = Thread
    fields = ['title']

    def form_valid(self, form):
        form.initial.author = self.request.user
        return super().form_valid(form)


def home(request):
    return render(request, 'forum/home.html', {})


def threads(request, t_id=None):
    if request.method == "GET":
        return _threads_no_auth(request, t_id=t_id)
    else:
        return _threads_auth(request, t_id=t_id)


def _threads_no_auth(request, t_id=None):
    if t_id is None:
        return render(request, 'forum/home.html')

    try:
        thread = Thread.objects.get(pk=int(t_id))
        next_exists = True
    except Thread.DoesNotExist:
        next_exists = False

    thread = get_object_or_404(Thread, id=int(t_id))  # don't want them to get a thread that doesn't exist now
    p = request.GET.get("p", default=1)
    data = {
            "thread": thread,
            "messages": thread.message_set.all(),
            "id": t_id,
            "page": p,

            # @TODO: Remove debug values
            "next_exists": next_exists,
            "next_page": int(p)+1,
            "next_id": int(t_id)+1
    }

    if int(p) > 1:
        data.update({"prev_page": int(p) - 1})
    if int(t_id) > 1:
        data.update({"prev_id": int(t_id) - 1})

    return render(request, 'forum/thread.html', data)

    elif request.method == "POST":
        if id is None:
            pass  # @TODO: Handle new thread creation
        else:
            pass  # @TODO: Handle new thread reply creation

    elif request.method == "DELETE":
        assert id is not None, "Thread deletion without id"
        # @TODO: Handle thread deletion

    elif request.method == "PATCH":
        assert id is not None, "Thread edit without id"
        # @TODO: Handle thread edit
