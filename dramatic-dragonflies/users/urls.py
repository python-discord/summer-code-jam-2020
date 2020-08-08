
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import register
from vmachine.views import vmachine_list, VMCreateView, VMDeleteView, create_floppy

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('register/', register, name="register"),
    path('disks/', vmachine_list, name="disks"),
    path('create_vm', VMCreateView.as_view(), name="create_new_vm"),
    path('delete_vm/<int:pk>', VMDeleteView.as_view(), name="delete_vm"),
    path('create_floppy', create_floppy, name="create_floppy")
]
