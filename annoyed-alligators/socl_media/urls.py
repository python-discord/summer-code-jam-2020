"""socl_media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from socl_media.apps.users import views as users_views

urlpatterns = [
    path('', include('socl_media.apps.feed.urls')),
    path('login/', auth_views.LoginView, name="login"),
    path('signup/', users_views.signup, name="signup"),
    path('logout/', auth_views.LogoutView, name="logout")
    path('home/', include('socl_media.apps.feed.urls')),
    path('admin/', admin.site.urls),
]
