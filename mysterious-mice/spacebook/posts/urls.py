from django.urls import path
from .views import ImagePostListView, ImagePostDetailView

urlpatterns = [
    path("home/", ImagePostListView.as_view(), name="posts-home"),
    path("post/<int:pk>", ImagePostDetailView.as_view(), name="posts-detail"),
]
