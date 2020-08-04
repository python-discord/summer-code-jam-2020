from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("upload/", views.upload, name="upload"),
    path("file/<str:name>/", views.fhandler, name="fhandler")
]
