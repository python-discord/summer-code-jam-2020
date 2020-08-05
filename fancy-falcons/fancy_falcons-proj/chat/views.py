from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

class UsersChatView(ListView):
    model = User
    template_name = 'chat/chat_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        user = get_object_or_404(get_user_model(), username=self.request.user)
        return get_user_model().objects.exclude(username=user)

