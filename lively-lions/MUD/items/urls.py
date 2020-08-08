from django.urls import path, include

urlpatterns = [
    path('items/', include('objects.urls')),
]
