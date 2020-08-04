from django.http import JsonResponse


def chat_lobby(request):
    return JsonResponse(dict())


def chat_room(request, room_name):
    return JsonResponse({'room_name': room_name})
