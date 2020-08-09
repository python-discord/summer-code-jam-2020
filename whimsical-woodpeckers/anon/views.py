import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from anon.models import AnonUser
import random
import string
from django.utils import timezone
# Create your views here.

def random_string(length):
    i = 0
    pw = ""
    while i < length:
        pw = pw+random.choice(string.printable)
        i += 1
    return pw


def get_user(user_id):
    try:
        return AnonUser.objects.get(id=user_id)
    except AnonUser.DoesNotExist:
        return None

def test(request):
    print(request.user)
    #return HttpResponse(AnonUser.objects)
    return HttpResponse(str(vars(request.user)))


def get_auth_token(request):
    auth_token = random_string(30)
    request.user.auth_token = auth_token
    request.user.auth_expiration = timezone.now() + datetime.timedelta(seconds=30)
    request.user.save()
    return JsonResponse({"token": auth_token})


def get_user_data(request):
    return JsonResponse({"id": request.user.id, "nickname": request.user.nickname})
