from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.home,
        name="forum-homepage"
    ),
    path(
        'forum/<str:tpc>/threads',
        views.topic,
        name="single-topic"
    ),
    path(
        'forum/<str:tpc>/threads/<int:pk>',  # tpc=topic
        views.threads,
        name='threads-single'
    ),
    path(
        'forum/<str:tpc>/threads/new',
        views.NewThread.as_view(),
        name="new-thread"
    ),
    path(
        'forum/<str:tpc>/threads/<int:pk>/edit',
        views.EditThread.as_view(),
        name="edit-thread"
    ),
    path(
        'forum/<str:tpc>/threads/<int:pk>/delete',
        views.DeleteThread.as_view(),
        name="delete-thread"
    ),
    path(
        'forum/<str:tpc>/threads/<int:pk>/new',
        views.NewMessage.as_view(),
        name="new-message"
    ),
    path(
        'forum/<str:tpc>/threads/<int:pk>/<int:msg_id>/edit',
        views.EditMessage.as_view(),
        name="edit-message"
    ),
    path(
        'forum/<str:tpc>/threads/<int:pk>/<int:msg_id>/delete',
        views.DeleteMessage.as_view(),
        name="delete-message"
    ),
]
