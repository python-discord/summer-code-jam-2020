from django.urls import path
from . import views

urlpatterns = [
	path('', views.get_posts),
	path('create', views.create_post),
	path('delete/<int:post_id>', views.delete_post),
	path('update/<int:post_id>', views.update_post),
]
