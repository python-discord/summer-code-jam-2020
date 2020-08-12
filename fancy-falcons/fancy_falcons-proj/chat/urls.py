from django.urls import path
from .views import (
    UsersChatView,
    UserChatRoom,
    CreateMessage,
    DeleteMessage,
)

app_name = 'chat'
urlpatterns = [
    path('', UsersChatView.as_view(), name='chat-list'),
    path('room/<int:pk>/', UserChatRoom.as_view(), name='chat-room'),
    path('room/<int:pk>/send', CreateMessage.as_view(), name='message-create'),
    path('room/<int:user_pk>/<int:pk>/delete', DeleteMessage.as_view(), name='message-delete'),
]
