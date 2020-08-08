from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random


# TODO Move this to a JSON file so it's easier to adjust and edit
list_of_hackers = ['Acid Burn', 'Phantom Phreak', 'Lord Nikon',
                   'The Plague', 'Zero Cool', 'Crash Override',
                   'Master of Disaster', 'Cereal Killer']


class Room(models.Model):
    name = models.CharField(max_length=50, default="Room")
    description = models.TextField(max_length=512)
    connections = models.ManyToManyField('self', blank=True)

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
        player_name = random.choice(list_of_hackers)  # TODO ensure some sort of uniqueness to this
        room_name = Room.objects.get(name='ARPANET-1')
        Player.objects.create_player(instance, player_name, room_name)
