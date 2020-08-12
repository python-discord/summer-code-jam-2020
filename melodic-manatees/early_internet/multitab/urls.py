from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.multitab_home,
        name='multitab-home'
        ),
    path(
        'edit_multitab/',
        views.add_multitab,
        name='edit-multitab'
        )
]
