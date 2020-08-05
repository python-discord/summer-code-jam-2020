from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.background_home,
        name='background-home'
        ),
    path(
        'delete_background/<int:pk>',
        views.delete_background,
        name='background-delete'
        ),
    path(
        'use_background/<int:pk>',
        views.use_background,
        name='background-use'
        ),
    path(
        'add_background/',
        views.add_background,
        name='add-background'
        )
]
