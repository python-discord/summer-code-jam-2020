from django.db import models


class Room(models.Model):
    # location coordinates of the room
    location_x = models.IntegerField()
    location_y = models.IntegerField()
    location_z = models.IntegerField()

    at_capacity = models.BooleanField(default=True)

    current_characters = []
    current_npcs = []

    def get_current_characters(self):
        return self.current_characters

    def character_in(self, character):
        self.current_characters.append(character)

    def get_floor(self):
        return self.location_z

    def character_out(self, character):
        char_index = self.current_characters.index(character)
        return self.current_characters.pop(char_index)


