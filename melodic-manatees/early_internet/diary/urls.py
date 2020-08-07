from django.urls import path

from . import views

urlpatterns = [
    path('', views.diary_entry_list, name='diary-list'),
    path('create/', views.diary_entry_create, name='diary-create'),
    path('<id>/', views.diary_entry_detail, name='diary-detail'),
    path('<id>/update/', views.diary_entry_update, name='diary-update'),
    path('<id>/delete/', views.diary_entry_delete, name='diary-delete'),
]
