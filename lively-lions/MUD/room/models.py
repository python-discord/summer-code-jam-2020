from django.db import models


class Room(models.Model):
    # location coordinates of the room
    location_x = models.IntegerField()
    location_y = models.IntegerField()
    location_z = models.IntegerField()

    # can someone enter the room
    has_room = models.BooleanField(default=True)

    # list of characters in the room
    current_characters = []
    # list of non-player-characters in room
    current_npcs = []

    # returns the list of characters in the room
    def get_current_characters(self):
        return self.current_characters

    # adds a character to the list current characters
    def character_in(self, character):
        self.current_characters.append(character)

    # returns the z access
    def get_floor(self):
        return self.location_z

    # removes character from the list and return the character object
    def character_out(self, character):
        char_index = self.current_characters.index(character)
        return self.current_characters.pop(char_index)
