from django.urls import path
from .views import UsersChatView

urlpatterns = [
    path('', UsersChatView.as_view(), name='chat-list'),
]