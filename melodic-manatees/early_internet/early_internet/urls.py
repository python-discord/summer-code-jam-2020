"""early_internet URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', user_views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='users/login.html'
            ),
        name='login'
    ),
    path('logout/', user_views.user_logout, name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('multitab/', include('multitab.urls')),
    path('diary/', include('diary.urls')),
    path('backgrounds/', include('background_app.urls')),
    path('news/', include('news.urls'))
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
