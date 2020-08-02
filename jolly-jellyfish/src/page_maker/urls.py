from django.urls import path

from .views import (
    MainView,
    UserRegister,
    UserDetailView,
    UserUpdateView,
    UserDeleteView
)

urlpatterns = [
    path('', MainView.as_view(), name='page-maker-main'),
    path('users/register', UserRegister.as_view(), name='register'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete', UserDeleteView.as_view(), name='user-delete'),
]
