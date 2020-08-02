from django.urls import path


from . import views


urlpatterns = [
    path('<str:text>/', views.process_command, name='command'),
]
