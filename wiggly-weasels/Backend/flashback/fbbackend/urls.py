from django.urls import path, include
from fbbackend import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('account', views.Account_View)
router.register('group', views.Group_View)
router.register



urlpatterns = [
    path('', include(router.urls))
]