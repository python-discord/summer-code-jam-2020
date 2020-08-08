from django.utils import timezone
from django.http import Http404
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Thread, Message, TOPICS


def home(request):
    return render(request, 'forum/home.html',
                  {'topics': TOPICS})


def topic(request, tpc=None):
    if tpc not in TOPICS:
        return render(request, 'forum/home.html', {'topics': TOPICS})

    the_topic = request.path.split(sep='/')[2]

    return render(request, 'forum/topic.html',
                  {'threads': reversed([t for t in Thread.objects.filter(topic=the_topic)]),
                   'topic': the_topic})


class NewThread(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic = self.request.path.split(sep='/')[2]
        form.save()
        form.instance.message_set.create(content=form.instance.content,
                                         thread=form.instance,
                                         author=self.request.user)
        form.instance.save()  # legit no idea why i gotta save twice

        self.pk = form.instance.id
        self.tpc = form.instance.topic

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('threads-single', kwargs={'pk': self.pk,
                                                 'tpc': self.tpc})


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

    def test_func(self):
        thread = self.get_object()
        return self.request.user == thread.author

    def get_success_url(self):
        return reverse('single-topic', kwargs={'tpc': self.request.path.split(sep='/')[2]})


class NewMessage(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # set the author to user
        thread_path = self.request.path.split(sep='/')  # parse which thread this was posted in
        form.instance.thread = Thread.objects.filter(pk=thread_path[-2]).first()

        self.id = form.instance.thread.id
        self.tpc = form.instance.thread.topic

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('threads-single', kwargs={'pk': self.id,
                                                 'tpc': self.tpc})


class EditMessage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Message
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date_edited = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('threads-single', kwargs={'pk': self.get_object().thread.id,
                                                 'tpc': self.get_object().thread.topic})

    def test_func(self):
        message = self.get_object()
        return self.request.user == message.author

    def get_object(self, queryset=None):
        path_list = self.request.path.split(sep='/')
        thread_id, msg_id = path_list[-3], path_list[-2]
        thread = get_object_or_404(Thread, pk=thread_id)
        try:
            msg = thread.message_set.get(pk=msg_id)
        except Message.DoesNotExist:
            raise Http404(f"Message with id {msg_id} does not exist in thread with id {thread_id}")
        return msg


class DeleteMessage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message

    def test_func(self):
        message = self.get_object()
        return self.request.user == message.author

    def get_success_url(self):
        return reverse('threads-single', kwargs={'tpc': self.get_object().thread.topic,
                                                 'pk': self.get_object().thread.id})

    def get_object(self, queryset=None):
        path_list = self.request.path.split(sep='/')
        thread_id, msg_id = path_list[-3], path_list[-2]
        thread = get_object_or_404(Thread, pk=thread_id)
        try:
            msg = thread.message_set.get(pk=msg_id)
        except Message.DoesNotExist:
            raise Http404(f"Message with id {msg_id} does not exist in thread with id {thread_id}")
        return msg


def threads(request, pk=None, tpc=None):
    if request.method == "GET":
        if pk is None or tpc not in TOPICS:
            return home(request)

        pk = int(pk)
        tpc = request.path.split(sep='/')[2]

        next_page = Thread.objects.filter(pk__gt=pk, topic=tpc).first()  # note: gt means greater than
        next_exists = bool(next_page)
        prev_page = Thread.objects.filter(pk__lt=pk, topic=tpc).last()  # and lt means less than
        prev_exists = bool(prev_page)

        thread = get_object_or_404(Thread, pk=pk, topic=tpc)  # don't want them to get a thread that doesn't exist now
        p = int(request.GET.get("p", default=1))
        data = {
            "thread": thread,
            "messages": thread.message_set.all(),
            "topic": tpc,
            "pk": pk,  # pk is for threads
            "page": p,
            "next_page": p + 1,
        }

        if p > 1:  # TODO: pagination (remove this todo by end of jam if not completed)
            data.update({"prev_page": p - 1})
        if prev_exists:
            data.update({"prev_pk": prev_page.pk})
        if next_exists:
            data.update({"next_pk": next_page.pk})

        return render(request, 'forum/thread.html', data)
