from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="home"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post/new/', views.PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name="post-delete")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
