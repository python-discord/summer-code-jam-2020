from django.urls import reverse, reverse_lazy
from django.views.generic.edit import (
    CreateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Message

class UsersChatView(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'chat/chat_list.html'
    context_object_name = 'users'
    login_url = 'login'

    def get_queryset(self):
        user = get_object_or_404(get_user_model(), first_name=self.request.user.first_name)
        return get_user_model().objects.exclude(first_name=user.first_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = "chat"
        last_message_list = []
        for user in context['users']:
            last_message = Message.objects.filter(
                (Q(reciever=self.request.user) & Q(sender=user)) |
                (Q(reciever=user) & Q(sender=self.request.user))
            ).order_by('-date')[:1].first()
            last_message_list.append(last_message)
            context['last_message'] = last_message_list
        return context


class UserChatRoom(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'chat/chat_room.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(
            (Q(sender=self.request.user) & Q(reciever=self.object)) |
            (Q(sender=self.object) & Q(reciever=self.request.user))
        ).order_by('date')
        context['active_page'] = "chat"
        return context


class CreateMessage(LoginRequiredMixin, CreateView):
    model = Message
    template_name = 'chat/message_create.html'
    fields = ['content']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.reciever = get_user_model().objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('chat:chat-room', kwargs={'pk': self.kwargs['pk']})


class DeleteMessage(DeleteView):
    model = Message
    template_name = 'chat/message_delete.html'

    def get_success_url(self):
        return reverse_lazy('chat:chat-room', kwargs={'pk': self.kwargs['user_pk']})
