from django.urls import path
from . import views

app_name = "forums"
urlpatterns = [
    path("", views.forumspage, name="home"),
    path("create_board/", views.BoardCreateView.as_view(), name="board-create"),
    path("<board>/", views.PostListView.as_view(), name="board-view"),
    path("user/<username>/", views.UserPostListView.as_view(), name="user-posts"),
    path("<board>/<int:pk>/", views.PostDetailView.as_view(), name="board-detail"),
    path("<board>/<int:post_pk>/<int:pk>/", views.CommentDetailView.as_view(), name="comment-detail"),
    path("<board>/<int:pk>/new/", views.CommentCreateView.as_view(), name="comment-create"),
    path("<board>/<int:post_pk>/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment-update"),
    path("<board>/<int:post_pk>/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
    path("<board>/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("<board>/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("<board>/new/", views.PostCreateView.as_view(), name="post-create"),
]
