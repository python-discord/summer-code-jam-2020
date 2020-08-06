from django.http import JsonResponse
from .models import Thread, ThreadMessage
from django.db.models import F
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from core.helpers import jsonbody


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


@jsonbody
def post_thread(request, data):
    current_user = request.user
    thread = Thread.objects.create(
        title=data['title'],
        created_by=current_user
    )
    thread_id = thread.id
    thread.save()

    message = ThreadMessage(
        message=data['message'],
        user=current_user,
        thread=thread
    )
    message.save()

    return JsonResponse({
        'thread_id': thread.id,
        'message': message.message,
        'user': message.user.username
    }, status=201)

@jsonbody
def post_message(request, data):
    current_user = request.user
    if data['message']:
        message = ThreadMessage(
        message=data['message'],
            user=current_user,
            thread=Thread.objects.get(id=data['thread_id'])
        )
        message.save()

    return JsonResponse({
        'thread_id': message.thread.id,
        'message': message.message,
        'user': message.user.username
    }, status=201)

def thread_details(request, thread_id):
    """
    View that returns all messages in a thread with a given id

    :param request:
    :param thread_id: ID of thread to filter on
    :return: JsonResponse
    """
    qs = ThreadMessage.objects.filter(thread_id=thread_id).values('date', 'message', 'user', title=F('thread__title'))
    data = list(qs)
    return JsonResponse(data, status=201, safe=False)
