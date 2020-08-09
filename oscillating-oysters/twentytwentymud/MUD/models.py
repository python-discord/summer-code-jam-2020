from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Server(models.Model):
    name = models.CharField(max_length=50, default="Server")
    server_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=50, default="Room")
    description = models.TextField(max_length=512)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='rooms', null=True)
    connections = models.ManyToManyField('self', blank=True, related_name='connects')
    command_description = models.TextField(max_length=512, blank=True)
    command_keyword = models.TextField(max_length=512, blank=True)
    command_response = models.TextField(max_length=512, blank=True)
    secret_connection_active = models.BooleanField(default=False)
    secret_room_connects = models.ManyToManyField('self', blank=True, symmetrical=False)
    next_server_connect = models.ManyToManyField(Server, blank=True)

    def __str__(self):
        return self.name


class PlayerManager(models.Manager):
    def create_player(self, user, name, room):
        player = self.create(name=name, user=user, room=room)
        return player


class Player(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    online = models.BooleanField(default=False)

    objects = PlayerManager()

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_player(sender, instance, created, **kwargs):
    '''
    Creates new player associated with newly created user account.
    Catches if user creates account through sign-up form.
    '''
    if created:
        player_name = instance.username
        try:
            room_name = Room.objects.get(name='ARPANET-1')
        except Room.DoesNotExist:
            Room.objects.create(name='ARPANET-1')
            room_name = Room.objects.get(name='ARPANET-1')
        try:
            Player.objects.get(name=player_name)
        except Player.DoesNotExist:
            Player.objects.create_player(instance, player_name, room_name)
