from django.shortcuts import render


def room(request):
    return render(request, 'prompt/room.html', {
        'room_name': 'mud'
    })
