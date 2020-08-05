from django.http import JsonResponse


def chat_lobby(request):
    return JsonResponse(dict())


def chat_room(request, room_name):
    return JsonResponse({'room_name': room_name})


def check_chat_room_name(request, room_name):
    is_valid = room_name.isalnum()
    message = 'Ok' if is_valid else 'Invalid chat room name. Names must be alphanumeric.'
    return JsonResponse({'valid': is_valid, 'message': message})
