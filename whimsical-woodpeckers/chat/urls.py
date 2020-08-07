from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='chat-home'),
    path('chat/', PostListView.as_view(), name='chat'),
    path('chat/<int:pk>/', PostDetailView.as_view(), name='chat-detail'),
    path('chat/new/', PostCreateView.as_view(), name='chat-create'),
    path('chat/<int:pk>/update/', PostUpdateView.as_view(), name='chat-update'),
    path('chat/<int:pk>/delete/', PostDeleteView.as_view(), name='chat-delete'),
]