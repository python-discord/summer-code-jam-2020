from django.urls import path
from . import views


urlpatterns = [
    path('<int:post_id>/', views.forum_post, name='viewpost'),
    path('post_forum_reply/<int:post_id>', views.forum_post_reply),
    path('', views.index, name='home')
]
