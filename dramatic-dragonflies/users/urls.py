
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import register
from vmachine.views import vmachine_list
urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('register/', register, name="register"),
    path('disks/', vmachine_list, name="disks")
]
