import datetime
# from django.shortcuts import render
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
        pw = pw + random.choice(string.printable)
        i += 1
    return pw


def get_user(user_id):
    try:
        return AnonUser.objects.get(id=user_id)
    except AnonUser.DoesNotExist:
        return None


def test(request):
    print(request.user)
    return HttpResponse(str(vars(request.user)))


def get_auth_token(request):
    auth_token = random_string(30)
    request.user.auth_token = auth_token
    request.user.auth_expiration = timezone.now() + datetime.timedelta(seconds=30)
    request.user.save()
    return JsonResponse({"token": auth_token})


def get_user_data(request):
    return JsonResponse({"id": request.user.id, "nickname": request.user.nickname})


def get_recent(request):
    recent = AnonUser.objects.filter(last_seen__gte=timezone.now() - datetime.timedelta(minutes=5))
    request.user.last_seen = timezone.now()
    request.user.save()
    return JsonResponse({'context': list(recent.values('id', 'nickname'))})
