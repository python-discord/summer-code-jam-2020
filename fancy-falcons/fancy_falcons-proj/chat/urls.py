from django.urls import path
from .views import (
    UsersChatView,
    UserChatRoom,
)

urlpatterns = [
    path('', UsersChatView.as_view(), name='chat-list'),
    path('room/<int:pk>/', UserChatRoom.as_view(), name='chat-room'),
]