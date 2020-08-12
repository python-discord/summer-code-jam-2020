from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Message


class ChatListView(LoginRequiredMixin, ListView):
    """
    View to display the messages received by the current user
    (Their message box)

    Provides access to message box only if logged in.
    Returns a queryset to display the most recent messages first.
    """

    template_name = 'chat/message-box.html'

    def get_queryset(self):
        queryset = Message.objects.filter(recipient=self.request.user).order_by('-sent_at')
        return queryset
