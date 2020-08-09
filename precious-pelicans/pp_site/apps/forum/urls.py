from django.urls import path

from . import views

urlpatterns = [
    path('<int:post_id>/vote', views.vote_post, name='vote-forum-post'),
    path('<int:post_id>/', views.forum_post, name='view-forum-post'),
    path('post_forum_reply/<int:post_id>/', views.forum_post_reply, name='post-forum-reply'),
    path('', views.index, name='home'),
    path('search/', views.search_posts, name='search-forum-posts'),
    path('upload/', views.upload_post, name='upload-forum-post')
]
