from django.shortcuts import render


def index(request):
    # Post-Friends model implementation:
    # context = {"friends": Friends.objects.all()}
    # return render(request, "blog/home.html", context)
    return render(request, "chat/index.html") 


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
