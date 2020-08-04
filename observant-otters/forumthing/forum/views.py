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
        thread_path = self.request.path.replace('/new', '')
        form.instance.thread = Thread.objects.filter(pk=int(thread_path[thread_path.rfind('/') + 1:])).first()
        return super().form_valid(form)


def threads(request, id=None):
    if request.method == "GET":
        if id is None:
            return render(request, 'forum/home.html')

        id = int(id)
        next_page = Thread.objects.filter(pk__gt=id).first()  # note: gt means greater than
        next_exists = bool(next_page)
        prev_page = Thread.objects.filter(pk__lt=id).last()  # and lt means less than
        prev_exists = bool(prev_page)

        thread = get_object_or_404(Thread, id=int(id))  # don't want them to get a thread that doesn't exist now
        p = int(request.GET.get("p", default=1))
        data = {
                "thread": thread,
                "messages": thread.message_set.all(),
                "id": id,
                "page": p,

                # @TODO: Remove debug values
                "next_page": p+1,
        }

        if p > 1:
            data.update({"prev_page": p - 1})
        if prev_exists:
            data.update({"prev_id": prev_page.pk})
        if next_exists:
            data.update({"next_id": next_page.pk})

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
