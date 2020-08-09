import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required


@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        'room_title': room_name,
    })
