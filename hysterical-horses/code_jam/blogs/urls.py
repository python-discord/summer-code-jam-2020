from django.urls import path

from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="blogs_list"),
    path("<int:pk>", views.BlogDetailView.as_view(), name="blog_detail"),
    path(
        "create/",
        views.PostCreateView.as_view(template_name="posts/create_post.html"),
        name="blog-create",
    ),
    path("like/<int:pk>", views.like_view, name="like_post"),
]
