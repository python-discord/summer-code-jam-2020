"""The game models."""
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import JSONField


class Location(models.Model):
    """A game location object."""

    x_coord = models.BigIntegerField(default=0, null=False)
    y_coord = models.BigIntegerField(default=0, null=False)
    z_coord = models.BigIntegerField(default=0, null=False)
    description = models.TextField()

    def __str__(self):
        return f"(x={self.x_coord}, y={self.y_coord}, z={self.z_coord})"


class NPC(models.Model):
    """A representation for NPCs."""

    class NPCTypes(models.TextChoices):
        MERCHANT = 'MC', _('Merchant')
        ENEMY = 'EN', _('Enemy')
        CIVILIAN = 'CV', _('Civilian')

    name = models.TextField()
    max_health = models.BigIntegerField(default=100)
    current_health = models.BigIntegerField(default=100)
    npc_type = models.CharField(max_length=2, choices=NPCTypes.choices, default=NPCTypes.ENEMY)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)


class Player(models.Model):
    """The player representation for a user."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.BigIntegerField(default=0)
    max_health = models.BigIntegerField(default=100)
    current_health = models.BigIntegerField(default=100)
    experience = models.BigIntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def move_to(self, new_location):
        self.location = new_location
        self.save()

    def level_up(self):
        self.level += 1
        self.save()


class ItemBlueprint(models.Model):
    '''The "blueprint" for items in the game.'''

    name = models.TextField()
    sell_price = models.BigIntegerField()
    buy_price = models.BigIntegerField()
    item_uses = models.BigIntegerField()
    consumable = models.BooleanField()
    item_function = models.TextField()
    item_kwargs = JSONField()


class ItemOwnership(models.Model):
    """Ownerhsip for an item."""

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(ItemBlueprint, on_delete=models.CASCADE)
    num_uses = models.BigIntegerField()
    equipped = models.BooleanField()
