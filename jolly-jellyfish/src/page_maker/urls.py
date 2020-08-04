from django.urls import path

from .views import (
    MainView,
    UserRegister,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    WebpageCreateView,
    WebpageView,
    WebpageDetailView,
    WebpageUpdateView,
    WebpageDeleteView,
    WebpageListView,
    TemplateCreateView,
    TemplateDeleteView,
    CommentCreateView,
    CommentDeleteView
)

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('users/register', UserRegister.as_view(), name='register'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete', UserDeleteView.as_view(), name='user-delete'),

    path('pages/new', WebpageCreateView.as_view(), name='webpage-create'),
    path('pages/<str:pagename>/', WebpageView.as_view(), name='webpage-view'),
    path('pages/<str:pagename>/detail', WebpageDetailView.as_view(), name='webpage-detail'),
    path('pages/<str:pagename>/update', WebpageUpdateView.as_view(), name='webpage-update'),
    path('pages/<str:pagename>/delete', WebpageDeleteView.as_view(), name='webpage-delete'),
    path('pages/', WebpageListView.as_view(), name='webpage-list'),

    path('pages/<str:pagename>/comment', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),

    path('templates/new', TemplateCreateView.as_view(), name='template-create'),
    path('templates/<int:pk>/delete', TemplateDeleteView.as_view(), name='template-delete'),
]
