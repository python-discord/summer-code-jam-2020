import logging
from django.http import JsonResponse
from core.helpers import jsonbody
from chat.models import _model_field_limits


logger = logging.getLogger(__name__)


def chat_lobby(request):
    return JsonResponse(dict())


def chat_room(request, room_name):
    return JsonResponse({'room_name': room_name})


@jsonbody
def check_chat_room_name(request, data):
    room_name = data.get('roomName')
    try:
        if not (isinstance(room_name, str) and room_name.isalnum()):
            message = 'Invalid chat room name. Names must be alphanumeric.'
            is_valid = False
        elif (0 > len(room_name) or len(room_name) > _model_field_limits['ChatRoom__name__max_length']):
            message = 'Invalid chat room name. Names must be between 1 and 20 characters.'
            is_valid = False
        else:
            message = 'Ok'
            is_valid = True
    except Exception:
        logger.exception('Error occurred in validating chat room name')
        message = 'An error occurred in going to the chat room, please contact an administrator'
        is_valid = False

    return JsonResponse({'valid': is_valid, 'message': message})
