from django.urls import path
from . import views

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login', views.signin, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.signout, name="logout")

]
