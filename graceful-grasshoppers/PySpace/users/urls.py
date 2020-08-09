from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.UserListView.as_view()),
    path("comment/", views.comment_on_profile),
    path("self/", views.LoggedInUserView.as_view()),
]
