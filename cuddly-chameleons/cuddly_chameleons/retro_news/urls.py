from django.urls import path
from rest_framework_simplejwt import views

from retro_news.views import CustomTokenObtainPairView, CustomUserCreate, LogOutView

urlpatterns = [
    path('token/obtain/', CustomTokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', CustomUserCreate.as_view(), name='create_user'),
    path('user/logout/', LogOutView.as_view(), name='logout'),
]
