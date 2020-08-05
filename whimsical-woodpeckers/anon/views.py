import datetime
from django.shortcuts import render
from django.http import HttpResponse
from anon.models import AnonUser

# Create your views here.


def get_user(user_id):
    try:
        return AnonUser.objects.get(id=user_id)
    except AnonUser.DoesNotExist:
        return None

def test(request):
    #return HttpResponse(AnonUser.objects)
    return HttpResponse(str(request.META))



