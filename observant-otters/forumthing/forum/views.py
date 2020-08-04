from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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
        form.instance.author = self.request.user
        print(self.request.path)
        # TODO: somehow get the thread from the current url
        return super().form_valid(form)


def threads(request, id=None):
    if request.method == "GET":
        if id is None:
            return render(request, 'forum/home.html')

        all_threads = list(map(lambda model: model.id, Thread.objects.all()))

        next_exists = all_threads[-1] != int(id)
        next_page = all_threads[all_threads.index(int(id)) + 1] if next_exists else None
        prev_exists = all_threads[0] != int(id)
        prev_page = all_threads[all_threads.index(int(id)) - 1] if prev_exists else None

        thread = get_object_or_404(Thread, id=int(id))  # don't want them to get a thread that doesn't exist now
        p = request.GET.get("p", default=1)
        data = {
                "thread": thread,
                "messages": thread.message_set.all(),
                "id": id,
                "page": p,

                # @TODO: Remove debug values
                "next_exists": next_exists,
                "next_page": int(p)+1,
                "next_id": next_page,  # really next THREAD
        }

        if int(p) > 1:
            data.update({"prev_page": int(p) - 1})
        if prev_exists:
            data.update({"prev_id": prev_page})

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
