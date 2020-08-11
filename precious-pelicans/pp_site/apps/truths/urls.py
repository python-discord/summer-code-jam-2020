from django.urls import path

from . import views

urlpatterns = [
    path('', views.truth_index, name='truth-index'),
    path('<int:truth_id>/', views.truth_post, name='truth-page'),
    path('upload/', views.upload_truth, name='upload-truth')
]
