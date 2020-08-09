from django.http import JsonResponse
from .models import Thread, ThreadMessage
from django.db.models import F
from django.contrib.auth.decorators import login_required

from core.helpers import jsonbody

# Set up SCHEMAS for fastjsonschema to validate response from frontend
SCHEMAS = {
    'thread_schema':
        {
            'type': 'object',
            'required': ['title', 'message'],
            'properties': {
                'title': {
                    'type': 'string',
                    'maxLength': 120,
                    'minLength': 3,

                },
                'message': {
                    'type': 'string',
                    'minLength': 2,
                    'maxLength': 3000
                }
            }
        },
    'message_schema':
        {
            'type': 'object',
            'required': ['message'],
            'properties': {
                'message': {
                    'type': 'string',
                    'minLength': 2,
                    'maxLength': 3000
                },
            }
        }
}


@login_required
def list_threads(request):
    """
    View that returns all threads as a json for being parsed by frontend

    :param request:
    :return: Serialized json data
    """
    queryset = Thread.objects.values().order_by('pk')
    data = list(queryset)

    return JsonResponse(data, status=201, safe=False)


@login_required
def thread_details(request, thread_id):
    """
    View that returns all messages in a thread with a given id

    :param request:
    :param thread_id: ID of thread to filter on
    :return: JsonResponse
    """
    queryset = ThreadMessage.objects.filter(thread_id=thread_id).values('date', 'message', 'user',
                                                                        title=F('thread__title'))
    data = list(queryset)

    return JsonResponse(data, status=201, safe=False)


@login_required
@jsonbody(SCHEMAS['thread_schema'])
def post_thread(request, data):
    """
    Accepts a title and a message as json and creates a new Thread and ThreadMessage object
    if data is valid according to SCHEMAS

    Returns thread_id, message and user if data is valid.
    Returns which schema rule is invalid and 400 if data invalid.

    :param request:
    :param data: Jsondata to process
    :return: A JSONResponse with message, user, thread if data valid
            else JSONReponse with error as string and status 400.
    """
    current_user = request.user
    thread = Thread.objects.create(
        title=data['title'],
        created_by=current_user
    )
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


@login_required
@jsonbody(SCHEMAS['message_schema'])
def post_message(request, data):
    """
    Accepts a thread_id and a message as json data and creates a new ThreadMessage object
    if data is valid according to SCHEMAS

    Returns thread_id, message and user if data is valid.
    Returns which schema rule is invalid and 400 if data invalid.

    :param request:
    :param data:
    :return: A JSONResponse with message, user, thread if data valid
            else JSONReponse with error as string and status 400.
    """
    current_user = request.user
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
