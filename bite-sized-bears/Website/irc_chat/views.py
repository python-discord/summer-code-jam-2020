from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'chat/index.html', {})


# @login_required # TODO: setup chat system
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
