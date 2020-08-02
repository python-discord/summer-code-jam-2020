from django.shortcuts import render


def index(request):
    return render(request, 'dashboard/index.html')


def chat_room(request, room_name):
    context = {'room_name': room_name}
    return render(request, 'dashboard/chat_room.html', context)
