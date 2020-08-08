from asgiref.sync import async_to_sync
from game.models import Player, Location


class Engine():
    def __init__(self, consumer):
        self.consumer = consumer

    @property
    def user(self):
        return self.consumer.user

    @property
    def player(self):
        return Player.objects.get(user=self.user)

    def gossip(self, gossip_content=None):
        if gossip_content is None:
            return "What do you want to gossip to the world?"

        self.__send(
            'global_message',
            f"{self.user} gossips: {gossip_content}"
        )

    def think(self, thought_content=None):
        """Think to yourself"""

        if thought_content is None:
            return "What the hell are you thinking about?"

        self.__send(
            'message_to_self',
            f"{self.user} thinks: {thought_content}",
            sender_channel_name=self.consumer.channel_name,
        )

    def look(self, *look_arg):
        if look_arg:
            parsed_look_arg = look_arg[0].split()
            if len(parsed_look_arg) == 1:
                look_target = parsed_look_arg[0]
                # todo: check if look_target is a player, item, monster, etc
                return f"You are looking at: {look_target}"
            else:
                return "'look' command only takes 1 argument. Please type 'look <target>'"
        else:
            # todo: look at place
            location_to_look = self.player.location
            players_at_location = Player.objects.filter(location=location_to_look)
            return f"You see:\n {location_to_look.description} \n {players_at_location}"

    def where(self):
        return f"You are here: {self.player.location.description} ({self.player.location})"

    def say(self, say_content=None):
        if say_content is None:
            return "What exactly do you want to say?"

        self.__send(
            'same_location_message',
            f"{self.user} says: {say_content}",
            location=f"{self.player.location}"
        )

    def start(self):
        if self.player.level == 0:
            start_location = Location.objects.get(x_coord=0, y_coord=0, z_coord=0)
            self.player.move_to(start_location)
            self.player.save()
            self.player.level_up()
            return "You are at the center of the world now!"
        else:
            return "This is no longer a valid command"

    def __move(self, direction):
        dest_x = self.player.location.x_coord
        dest_y = self.player.location.y_coord
        dest_z = self.player.location.z_coord

        direction = direction.lower()

        if direction == 'north':
            dest_y += 1

        elif direction == 'south':
            dest_y -= 1

        elif direction == 'east':
            dest_x += 1

        elif direction == 'west':
            dest_x -= 1

        elif direction == 'up':
            dest_z += 1

        elif direction == 'down':
            dest_z -= 1

        try:
            dest_location = Location.objects.get(x_coord=dest_x, y_coord=dest_y, z_coord=dest_z)
            self.__send(
                'same_location_message',
                f"{self.user} left the area",
                location=f"{self.player.location}",
            )
            self.player.move_to(dest_location)
            self.__send(
                'same_location_message_not_me',
                f"{self.user} just arrived",
                location=f"{self.player.location}",
                sender_channel_name=self.consumer.channel_name,
            )
        except Location.DoesNotExist:
            return False

        return True

    def north(self):
        if self.__move('north'):
            return "You move to the north"
        else:
            return "You can't go north from here"

    def south(self):
        if self.__move('south'):
            return "You move to the south"
        else:
            return "You can't go south from here"

    def east(self):
        if self.__move('east'):
            return "You move to the east"
        else:
            return "You can't go east from here"

    def west(self):
        if self.__move('west'):
            return "You move to the west"
        else:
            return "You can't go west from here"

    def up(self):
        if self.__move('up'):
            return "You move up"
        else:
            return "You can't go up from here"

    def down(self):
        if self.__move('down'):
            return "You move down"
        else:
            return "You can't go down from here"

# Shortcuts to move methods

    n = north
    s = south
    e = east
    w = west
    u = up
    d = down

    def help(self, command_to_help=None):
        """If you use 'help' you can see a list of availlable commands.
        You can also use 'help <command>' to get a more specific guide."""

        methods_list = [
            func for func in dir(Engine)
            if (callable(getattr(Engine, func)) and not func.startswith("_") and len(func) > 1)
        ]
        if command_to_help is None:
            message = "This is the list of all commands available in this server:"
            for func in methods_list:
                message = message + f"\n{func!r}"
            return message
        else:
            if command_to_help in methods_list:
                help_text = getattr(Engine, command_to_help).__doc__
                return f"This is the 'help' for {command_to_help!r}: {help_text}"
            else:
                return f"{command_to_help!r} is not a valid command. We can't help you with that."
        # todo: validation for too long input

    def __send(self, type, message, **kwargs):
        sending_event = {
            'type': type,
            'message': message,
        }
        for k, val in kwargs.items():
            sending_event[k] = val
        async_to_sync(self.consumer.channel_layer.group_send)(
            self.consumer.room_group_name, sending_event)
