from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Room
from .forms import RoomNameForm

def index(request):
    return render(request, "chat/index.html")

def room(request, room_name: str):
    return render(request, "chat/room.html", {
        'room_name': room_name
    })

def create_room(request):
    """
    Adds a room specified in a form.
    """
    if request.method == 'POST':
        form = RoomNameForm(request.POST)
        if form.is_valid():
            Room(name=form.cleaned_data).save()
            return HttpResponseRedirect('/chat/rooms/')
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
    return render(request, "chat/rooms.html", {
        "rooms": rooms,
    })