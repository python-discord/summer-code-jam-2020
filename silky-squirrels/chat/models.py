from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RoomMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"room='{self.room}' user='{self.user}' active= '{self.active}''"


class Message(models.Model):
    room_member = models.ForeignKey(RoomMember, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return (
            f"user='{self.room_member.user.username}' room='{self.room}' text='{self.text}' "
            f"timestamp='{self.timestamp}'"
        )
