from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_threads, name='threads'),
    path('<thread_id>/', views.thread_details, name='thread-details')
]
