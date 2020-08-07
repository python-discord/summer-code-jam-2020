from django.http import JsonResponse
from core.helpers import jsonbody


def chat_lobby(request):
    return JsonResponse(dict())


def chat_room(request, room_name):
    return JsonResponse({'room_name': room_name})


@jsonbody
def check_chat_room_name(request, data):
    room_name = data.get('roomName')
    is_valid = isinstance(room_name, str) and room_name.isalnum()
    message = 'Ok' if is_valid else 'Invalid chat room name. Names must be alphanumeric.'
    return JsonResponse({'valid': is_valid, 'message': message})
