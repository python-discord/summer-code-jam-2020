from django.urls import path

from . import views

app_name = 'mailmessages'
urlpatterns = [
    path('', views.list_messages, name='inbox'),
    path('usernames/', views.get_users, name='usernames'),
    path('post/message/', views.post_message, name='mail-details'),
]
