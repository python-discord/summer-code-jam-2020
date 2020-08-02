from django.urls import path

from .views import sms_reply

urlpatterns = [
    path('', sms_reply, name='sms_reply')
]
