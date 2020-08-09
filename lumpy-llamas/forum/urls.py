from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.list_threads, name='threads'),
    path('<int:thread_id>', views.thread_details, name='thread-details'),
    path('post/thread', views.post_thread, name='new-thread'),
    path('post/message', views.post_message, name='new-thread'),
]
