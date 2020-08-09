from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class MudUser(User):
    now_connected_character_name = models.TextField(max_length=100, default='', blank=True, null=True,)

    def create_character(self, name: str):
        pass


# hp/attack/defense depends on : equiped item / Special Permanent enhancement(or Decline) item.
# Damage Formula : attack*(100/(100+defense))
# ADD attack_cool_time
class Character(models.Model):
    name = models.TextField(max_length=100, unique=True)
    user = models.ForeignKey('MudUser', on_delete=models.CASCADE)
    hp = models.IntegerField(default=100)
    max_hp = models.IntegerField(default=100)
    total_attack = models.IntegerField(default=11)
    total_defense = models.IntegerField(default=11)
    attack_cool_time = models.FloatField(default=3.0)
    location_x = models.IntegerField(default=1)
    location_y = models.IntegerField(default=1)
    location_z = models.IntegerField(default=1)

#     def increase_health(self, health):
#         """Increase health
#         Args:
#             health ([type]): [description]
#         """
#         pass

#     def decrease_health(self, health):
#         """[summary]
#         Args:
#             health ([type]): [description]
#         """
#         pass

#     def equip_item(self, item):
#         """Equip item
#         Args:
#             item ([type]): [description]
#         """
#         pass

#     def unequip_item(self, item):
#         """Unequip item
#         Args:
#             item ([type]): [description]
#         """
#         pass

#     # def pickup_item(self, item):
#     #     """Pick up item

#     #     Args:
#     #         item ([type]): [description]
#     #     """
#     #     pass

#     # def look_at(self, object):
#     #     """Look at object

#     #     Args:
#     #         object ([type]): [description]
#     #     """
#     #     pass

#     def move(self, direction):
#         """Move with direction
#         Args:
#             direction ([type]): [description]
#         """
#         pass

#     # def move_to(self, object):
#     #     """Move to an object

#     #     Args:
#     #         object ([type]): [description]
#     #     """
#     #     pass

#     # def interact(self, object):
#     #     """Interact with object

#     #     Args:
#     #         object ([type]): [description]
#     #     """
#     #     pass
