from django.contrib.auth.models import User
# from django.db import models


# Create your models here.
class MudUser(User):
    def create_character(self, name: str):
        pass


# class Character(models.Model):
#     name = models.TextField(max_length=100)
#     min_health = 0
#     max_health = models.IntegerField()
#     health = models.IntegerField()
#     speed = models.IntegerField()
#     user = models.ForeignKey('MudUser', on_delete=models.CASCADE)
#     # TODO: add location

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
