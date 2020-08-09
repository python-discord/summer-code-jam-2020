from django.urls import path, include
from rest_framework import routers

from . import views

# use automatic router for ViewSets
router = routers.DefaultRouter()
router.register(r'boards', views.BoardViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

app_name = 'nchan'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
