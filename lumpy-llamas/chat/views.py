import logging
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from core.helpers import jsonbody
from chat.models import _model_field_limits


logger = logging.getLogger(__name__)


@login_required
def chat_lobby(request):
    return JsonResponse(dict())


@login_required
def chat_room(request, room_name):
    return JsonResponse({'room_name': room_name})


CHAT_ROOM_SCHEMA = {
    'type': 'object',
    'required': ['roomName'],
    'properties': {
        'roomName': {
            'type': 'string',
            'maxLength': _model_field_limits['ChatRoom__name__max_length'],
            'minLength': 1,
        },
    },
}


@login_required
@jsonbody(CHAT_ROOM_SCHEMA)
def check_chat_room_name(request, data):
    room_name = data.get('roomName')
    try:
        if not room_name.isalnum():
            message = 'Invalid chat room name. Names must be alphanumeric.'
            is_valid = False
        else:
            message = 'Ok'
            is_valid = True
    except Exception:
        logger.exception('Error occurred in validating chat room name')
        message = 'An error occurred in going to the chat room, please contact an administrator'
        is_valid = False

    return JsonResponse({'valid': is_valid, 'message': message})
