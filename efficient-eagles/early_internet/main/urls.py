from django.urls import path
from main import views  # to prevent namespace pollution


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('create/topic', views.CreateTopicView.as_view(), name='create_topic'),
    path('topic/<str:topic_name>/', views.TopicView.as_view(), name='topic'),
    path('topic/<str:topic_name>/<slug:slug>', views.InfoView.as_view(), name='info'),
    path('create/post', views.CreatePostView.as_view(), name='create_post'),
    path('search/<str:q>', views.SearchView.as_view(), name='search'),
]
