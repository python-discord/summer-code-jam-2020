from django.shortcuts import render
from .models import Message
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.


class ChatListView(LoginRequiredMixin, ListView):
    """
    Provide access to message box only after login.
    Return a queryset to display the most recent messages.
    """
    template_name = 'chat/message-box.html'

    def get_queryset(self):
        queryset = Message.objects.filter(recipient=self.request.user).order_by('-sent_at')
        return queryset
