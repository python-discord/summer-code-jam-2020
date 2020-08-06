from django.http import JsonResponse
from .models import Thread, ThreadMessage
from django.db.models import F
from django.contrib.auth.models import User
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

#@login_required
@jsonbody
def post_thread(request, data):
    current_user = request.user
    if data:
        thread = Thread.objects.create(
            title=data['title'],
            created_by=User.objects.get(id=current_user.id)
        ).save()
        id = thread
        print(id)
        thread_message = Thread(
            message=data['message'],
            user_id=request.user,
            thread_id=id.id
        ).save()
        #login(request, user)
        print(thread)
        return JsonResponse({
            'title': thread.title,
            'user': thread.created_by.username,
        }, status=201)
    return {'title': 'Not a valid title', 'message': 'Not a valid message'}

def thread_details(request, thread_id):
    """
    View that returns all messages in a thread with a given id

    :param request:
    :param thread_id: ID of thread to filter on
    :return: JsonResponse
    """
    qs = ThreadMessage.objects.filter(thread_id=thread_id).values('date', 'message', 'user', title=F('thread__title'))
    print(str(qs.query))
    data = list(qs)
    print(data)
    return JsonResponse(data, status=201, safe=False)
