from django.urls import path
from main.views import (
    HomeView,
    LoginView,
    LogoutView,
    RegisterView,
    CreateTopicView,
    TopicView,
    InfoView,
    CreatePostView,
    SearchView,
    UserView,
)


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("create/topic", CreateTopicView.as_view(), name="create_topic"),
    path("topic/<str:name>/", TopicView.as_view(), name="topic"),
    path("topic/<str:name>/<slug:slug>", InfoView.as_view(), name="info"),
    path("create/post", CreatePostView.as_view(), name="create_post"),
    path("search/<str:q>", SearchView.as_view(), name="search"),
    path('user/<str:user>', UserView.as_view(), name='profile'),
    path('user/<str:user>/posts', UserView.as_view())
]
