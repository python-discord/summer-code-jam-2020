from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from chat.forms import RoomCreationForm
from chat.models import Room, RoomMember, Message
from users.models import Profile


@login_required
def index(request):
    if request.method == "POST":
        form = RoomCreationForm(request.POST)
        if form.is_valid():
            room_name = form.cleaned_data["name"]
            Room.objects.get_or_create(name=room_name)
            return redirect("room", room_name)

    else:
        form = RoomCreationForm()

    context = {
        "form": form,
        "friends": Profile.objects.get(user=request.user).friends.all(),
    }

    return render(request, "chat/index.html", context)


@login_required
def room(request, room_name, *args):
    try:
        room = Room.objects.get(name=room_name)
        room_member, room_member_created = RoomMember.objects.get_or_create(user=request.user, room=room)
        active_room_members = RoomMember.objects.filter(room=room, active=True)
    except (Room.DoesNotExist):
        messages.warning(request, f"Room not found: {room_name}")
        return redirect("chat")
    older_messages = reversed(Message.objects.filter(room=room).order_by("-timestamp")[:19])
    context = {
            "room_name": room.name,
            "room_member_id": room_member.id,
            "older_messages_text": "\n".join(
                f"[{older_message.timestamp}] {older_message.room_member.user.username}: {older_message.text}"
                for older_message in older_messages
            ),
            "active_room_members": active_room_members,
            "curr_username": request.user.username,
            }
    if args:
        context['pvt_members'] = args
    return render(request, "chat/room.html", context=context)


@login_required
def froom(request, user_id, friend_id):
    ids = (user_id, friend_id)
    room_name = f'{min(ids)}-{max(ids)}'
    if request.user.id in ids:
        r, room_created = Room.objects.get_or_create(name=room_name)
        RoomMember.objects.get_or_create(user=request.user, room=r)
        return room(request, room_name, User.objects.get(id=user_id), User.objects.get(id=friend_id))
    else:
        messages.warning(request, f"Chatroom doesn't exist. Try befriending {User.objects.get(id=friend_id)}!")
        return redirect("chat")
