from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from chat.forms import RoomCreationForm
from chat.models import Room, RoomMember, Message


@login_required
def index(request):
    # Post-Friends model implementation:
    # context = {"friends": Friends.objects.all()}
    # return render(request, "blog/home.html", context)
    if request.method == "POST":
        form = RoomCreationForm(request.POST)
        if form.is_valid():
            room_name = form.cleaned_data["name"]
            room, room_created = Room.objects.get_or_create(name=room_name)
            RoomMember.objects.get_or_create(user=request.user, room=room)
            return redirect("room", room_name)
    else:
        form = RoomCreationForm()
    return render(request, "chat/index.html", {"form": form})


@login_required
def room(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
        room_member = RoomMember.objects.get(user=request.user, room=room)
        active_room_members = RoomMember.objects.filter(room=room, active=True)
    except (Room.DoesNotExist, RoomMember.DoesNotExist):
        messages.warning(request, f"Room not found: {room_name}")
        return redirect("chat")
    older_messages = reversed(Message.objects.filter(room=room).order_by("-timestamp")[:19])
    return render(
        request,
        "chat/room.html",
        {
            "room_name": room.name,
            "room_member_id": room_member.id,
            "older_messages_text": "\n".join(
                f"{older_message.room_member.user.username}: {older_message.text}" for older_message in older_messages
            ),
            "active_room_members": active_room_members,
            "curr_username": request.user.username,
        },
    )
