from django.urls import path, re_path
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
      'forum/threads/<int:id>',
      views.threads,
      name='threads-single'
    ),
    path(
        'forum/threads/new',
        views.NewThread.as_view(),
        name="new-thread"
    ),
]
