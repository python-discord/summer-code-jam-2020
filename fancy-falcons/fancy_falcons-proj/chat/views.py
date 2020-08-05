from django.urls import reverse, reverse_lazy
from django.views.generic.edit import (
    CreateView,
    DeleteView,
)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Message

class UsersChatView(ListView):
    model = User
    template_name = 'chat/chat_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        user = get_object_or_404(get_user_model(), username=self.request.user)
        return get_user_model().objects.exclude(username=user)


class UserChatRoom(DetailView):
    model = User
    template_name = 'chat/chat_room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(
            (Q(sender=self.request.user) & Q(reciever=self.object)) |
            (Q(sender=self.object) & Q(reciever=self.request.user))
        ).order_by('-date')
        return context


class CreateMessage(CreateView):
    model = Message
    template_name = 'chat/message_create.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.reciever = get_user_model().objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('chat-room', kwargs={'pk': self.kwargs['pk']})


class DeleteMessage(DeleteView):
    model = Message
    template_name = 'chat/message_delete.html'

    def get_success_url(self):
        return reverse_lazy('chat-room', kwargs={'pk': self.kwargs['user_pk']})