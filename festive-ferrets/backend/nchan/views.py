from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from .models import *


# Create your views here.

def index(request):
    return HttpResponse('Index loaded successfully')


def get_boards(request):
    data = {
        'boards': list(Board.objects.all().values('name'))
    }
    return JsonResponse(data)
