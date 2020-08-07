from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Room
from .services import MessageService, RoomService


def index(request):
    return render(request, "chat/index.html", context={"rooms": Room.objects.all()})


def room(request, room_id: int):
    # If room exists then give it and its messages to context
    room_from_db = RoomService.get_room_by_id(room_id)
    if room_from_db is not None:
        messages = MessageService.get_distinct_messages()
        return render(request, "chat/room.html", {
            'room': room_from_db,
            'messages': messages,
        })
    else:
        return HttpResponseNotFound("<h1>Room not found!</h1>")
