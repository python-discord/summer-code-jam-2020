from django.urls import path
from django.conf.urls import include

from rest_framework import routers
from rest_framework_simplejwt import views

from retro_news.views import CustomTokenObtainPairView, CustomUserCreate, LogOutView, BlogArticleViewSet
from retro_news.models import BlogArticle

router = routers.DefaultRouter()
router.register(r'blogs', BlogArticleViewSet, basename='BlogArticle')

urlpatterns = [
    path('token/obtain/', CustomTokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', CustomUserCreate.as_view(), name='create_user'),
    path('user/logout/', LogOutView.as_view(), name='logout'),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('blogs/',include(router.urls)),
]
