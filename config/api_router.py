from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from shiny_sheep.users.api.views import CreateUserView, UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('users', UserViewSet)


app_name = "api"
urlpatterns = [
    path('register/', CreateUserView.as_view())
]
urlpatterns += router.urls
