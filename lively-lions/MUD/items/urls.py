from django.urls import path, include

urlpatterns = [
    # will be changed later this was for flake8
    path('items/', include('objects.urls')),
]
