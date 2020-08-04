from django.http import JsonResponse
import logging
from .models import Thread, ThreadMessage

# Create your views here.

def list_threads(request):
    """
    View that returns all threads as a json

    :param request:
    :return: Serialized json data
    """

    qs = Thread.objects.values().order_by('pk')
    data = list(qs)

    return JsonResponse(data, status=201, safe=False)



def post_thread(request):
    pass


def thread_details(request, thread_id):
    """
    View that returns all messages in a thread with a given id

    :param request:
    :param thread_id: ID of thread to filter on
    :return: JsonResponse
    """
    qs = ThreadMessage.objects.select_related('thread').filter(thread_id=thread_id).values()
    data = list(qs)
    return JsonResponse(data, status=201, safe=False)

