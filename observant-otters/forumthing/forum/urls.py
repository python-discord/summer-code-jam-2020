from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.home,
        name="forum-homepage"
    ),
    path(
        'forum/threads',
        views.threads,
        name="threads-all"
    ),
    path(
      'forum/threads/<int:t_id>',
      views.threads,
      name='threads-single'
    ),
    path(
        'forum/threads/new',
        views.NewThread.as_view(),
        name="new-thread"
    ),
    path(
        'forum/threads/<int:t_id>/new',
        views.NewMessage.as_view(),
        name="new-message"
    ),
]
