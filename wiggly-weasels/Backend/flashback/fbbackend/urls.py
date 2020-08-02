from django.urls import path, include
from fbbackend import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('account', views.Account_View)
router.register('group', views.Account_View)
router.register('message', views.Message_View)
router.register('forum_post', views.Post_View)

urlpatterns = [
    path('', include(router.urls))
]