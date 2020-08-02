from django.shortcuts import render
from django.views.generic import ListView
from .models import Thread, ThreadMessage
from django.utils import timezone
from django.core import serializers
from django.contrib.staticfiles.views import serve
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.

def list_threads(request):
    """
    View that returns all threads as a json

    :param request:
    :return: Serialized json data
    """

    context = {
        "name": "threads",
        "serialized_data": serializers.serialize("json", Thread.objects.all()),
        "count": Thread.objects.all().count()
    }
    return JsonResponse(context, status=201)


def post_thread(response):
    pass


def thread_details(request, thread_id):
    """
    View that returns all messages in a thread with a given id

    :param request:
    :param thread_id: ID of thread to filter on
    :return: Serialized json
    """

    context = {
        "name": "threads",
        "serialized_data": serializers.serialize("json", ThreadMessage.objects.filter(pk=thread_id)),
        "count": ThreadMessage.objects.all().count()
    }
    return JsonResponse(context, status=201)
