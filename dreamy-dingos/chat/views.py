from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Room
from .models import SimpleUser
from .forms import RoomNameForm
from .forms import LoginForm
from .services import MessageService, RoomService


def index(request):
    return render(request, "chat/index.html", context={"rooms": Room.objects.all()})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            SimpleUser(username=form.cleaned_data).save()
            return HttpResponseRedirect('/chat/rooms/')
    else:
        form = LoginForm()
    return render(request, 'chat/login.html', {'form': form})


def room(request, room_id: int):
    # If room exists then give it and its messages to context
    room_from_db = RoomService.get_room_by_id(room_id)
    if room_from_db is not None:
        messages = MessageService.get_distinct_messages(room_id)
        return render(request, "chat/room.html", {
            'room': room_from_db,
            'messages': messages,
        })
    else:
        return HttpResponseNotFound("<h1>Room not found!</h1>")


def create_room(request):
    """
    Adds a room specified in a form.
    """
    if request.method == 'POST':
        form = RoomNameForm(request.POST)
        if form.is_valid():
            Room(name=form.cleaned_data).save()
            return HttpResponseRedirect('/rooms/')
    else:
        form = RoomNameForm()
    return render(request, 'chat/rooms.html', {'form': form})


def remove_room(request, name):
    """
    Removes a room from rooms table.
    """
    Room.objects.remove(name=name)


def all_rooms(request):
    """
    Returns all rooms.
    """
    rooms = Room.objects.all()
    return render(request, "chat/rooms.html", {'rooms': rooms}) 
