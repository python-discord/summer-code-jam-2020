from django.shortcuts import render


# Will need to implement the Friends model    
def index(request):
    # context = {"friends": Friends.objects.all()}
    return render(request, "chat/index.html") 
    #return render(request, "blog/home.html", context)

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
