from django.urls import path
from main.views import HomeView, LoginView, LogoutView, RegisterView, CreateTopicView, TopicView, InfoView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('createtopic/', CreateTopicView.as_view(), name='create_topic'),
    path('topic/<str:topic_name>/', TopicView.as_view(), name='topic'),
    path('topic/<str:topic_name>/<slug:slug>', InfoView.as_view(), name='info'),
]
