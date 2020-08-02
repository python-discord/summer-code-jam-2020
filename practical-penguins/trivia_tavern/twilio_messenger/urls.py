from django.urls import path

from .views import sms_send

urlpatterns = [
    path('', sms_send, name='sms_send')
]
