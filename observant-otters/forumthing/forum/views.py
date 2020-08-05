from django.utils import timezone
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Thread, Message


def home(request):
    return render(request, 'forum/home.html', {})


class NewThread(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        form.instance.message_set.create(content=form.instance.content,
                                         thread=form.instance,
                                         author=self.request.user)
        form.instance.save()  # legit no idea why i gotta save twice
        return super().form_valid(form)


class EditThread(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Thread
    fields = ['title', 'content']

    def form_valid(self, form):
        first_message = form.instance.message_set.all()[0]
        first_message.content = form.instance.content
        first_message.save()
        return super().form_valid(form)

    def test_func(self):
        thread = self.get_object()
        return self.request.user == thread.author


class DeleteThread(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Thread
    success_url = '/'

    def test_func(self):
        thread = self.get_object()
        return self.request.user == thread.author


class NewMessage(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # set the author to user
        thread_path = self.request.path.replace('/new', '')  # parse which thread this was posted in
        form.instance.thread = Thread.objects.filter(pk=int(thread_path[thread_path.rfind('/') + 1:])).first()
        return super().form_valid(form)


class EditMessage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Message
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date_edited = timezone.now()
        return super().form_valid(form)

    def test_func(self):
        message = self.get_object()
        return self.request.user == message.author


class DeleteMessage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    success_url = '/forum/threads/2'

    def test_func(self):
        message = self.get_object()
        return self.request.user == message.author

    def get_success_url(self):
        return reverse('threads-single', urlconf={'pk': self.get_object().thread.id})


def threads(request, id=None):
    pk = id
    if request.method == "GET":
        if pk is None:
            return render(request, 'forum/home.html')

        pk = int(pk)
        next_page = Thread.objects.filter(pk__gt=pk).first()  # note: gt means greater than
        next_exists = bool(next_page)
        prev_page = Thread.objects.filter(pk__lt=pk).last()  # and lt means less than
        prev_exists = bool(prev_page)

        thread = get_object_or_404(Thread, pk=pk)  # don't want them to get a thread that doesn't exist now
        p = int(request.GET.get("p", default=1))
        data = {
                "thread": thread,
                "messages": thread.message_set.all(),
                "pk": pk,  # pk is for threads
                "page": p,

                # @TODO: Remove debug values
                "next_page": p+1,
        }

        if p > 1:
            data.update({"prev_page": p - 1})
        if prev_exists:
            data.update({"prev_pk": prev_page.pk})
        if next_exists:
            data.update({"next_pk": next_page.pk})

        return render(request, 'forum/thread.html', data)

    elif request.method == "POST":
        if pk is None:
            pass  # @TODO: Handle new thread creation
        else:
            pass  # @TODO: Handle new thread reply creation

    elif request.method == "DELETE":
        assert pk is not None, "Thread deletion without id"
        # @TODO: Handle thread deletion

    elif request.method == "PATCH":
        assert pk is not None, "Thread edit without id"
        # @TODO: Handle thread edit
