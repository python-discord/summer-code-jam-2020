from django.urls import path

from . import views

urlpatterns = [
    path('', views.ThreadListView.as_view(), name='index'),
]