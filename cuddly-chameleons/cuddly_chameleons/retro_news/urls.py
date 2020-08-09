from django.urls import path
from rest_framework_simplejwt import views

from retro_news import views as retro_views

urlpatterns = [
    path('token/obtain/', retro_views.CustomTokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', retro_views.CustomUserCreate.as_view(), name='create_user'),
    path('user/logout/', retro_views.LogOutView.as_view(), name='logout'),
    path('posts/', retro_views.BlogArticleListView.as_view(), name='posts'),
    path('posts/<int:pk>/', retro_views.BlogArticleActionView.as_view(), name='post'),
    path('superuser/', retro_views.IsSuperUserView.as_view(), name='is_superuser'),
    path('comments/', retro_views.ArticleCommentListView.as_view(), name='comments')
]
