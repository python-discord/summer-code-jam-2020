import json

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import *


# Create your views here.

def index(request):
    return HttpResponse('Index loaded successfully')


def get_boards(request):
    data = {
        'boards': list(Board.objects.all().values())
    }
    return JsonResponse(data)


@csrf_exempt
def add_board(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Board(name=data["name"], post_num=data["post_num"]).save()
    return HttpResponse("OK")
