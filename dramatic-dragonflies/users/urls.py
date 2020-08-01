
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
urlpatterns = [
    path('login/', LoginView.as_view(template_name="")),
    path('logout/', LogoutView.as_view(template_name=""))
]
