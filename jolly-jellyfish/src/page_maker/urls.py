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
    TemplateView,
    TemplateDeleteView,
    TemplateDetailView,
    TemplateListView,
    CommentCreateView,
    CommentDeleteView
)

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('users/register', UserRegister.as_view(), name='register'),
    path('users/<str:username>', UserDetailView.as_view(), name='user-detail'),
    path('users/<str:username>/update', UserUpdateView.as_view(), name='user-update'),
    path('users/<str:username>/delete', UserDeleteView.as_view(), name='user-delete'),

    path('pages/new', WebpageCreateView.as_view(), name='webpage-create'),
    path('pages/<str:pagename>', WebpageView.as_view(), name='webpage-view'),
    path('pages/<str:pagename>/detail', WebpageDetailView.as_view(), name='webpage-detail'),
    path('pages/<str:pagename>/update', WebpageUpdateView.as_view(), name='webpage-update'),
    path('pages/<str:pagename>/delete', WebpageDeleteView.as_view(), name='webpage-delete'),
    path('pages-recent', WebpageListView.as_view(ordering='-date_created'), name='webpage-list-recent'),
    path('pages-top', WebpageListView.as_view(ordering='-like_count'), name='webpage-list-top'),

    path('pages/<str:pagename>/comment', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),

    path('templates', TemplateListView.as_view(), name='template-list'),
    path('templates/new', TemplateCreateView.as_view(), name='template-create'),
    path('templates/<str:templatename>', TemplateView.as_view(), name='template-view'),
    path('templates/<str:templatename>/detail', TemplateDetailView.as_view(), name='template-detail'),
    path('templates/<str:templatename>/delete', TemplateDeleteView.as_view(), name='template-delete'),
]
