from asgiref.sync import async_to_sync
from game.models import Player, Location

class Engine():
    def __init__(self, consumer, command_line):
        self.consumer = consumer
        self.command_line = command_line
        self.user = consumer.user
        self.player = Player.objects.get(user_id=self.user)

    def gossip(self):
        if len(self.command_line.split(maxsplit=1)) == 2:
            gossip_content = self.command_line.split(maxsplit=1)[1]
            async_to_sync(self.consumer.channel_layer.group_send)(
                self.consumer.room_group_name,
                {
                    'type': 'global_message_login_required',
                    'message': f"{self.user} gossips: {gossip_content}",
                }
            )
            return False
        else:
            return "What do you want to gossip to the world?"

    def think(self):
        if len(self.command_line.split(maxsplit=1)) == 2:
            thought_content = self.command_line.split(maxsplit=1)[1]
            async_to_sync(self.consumer.channel_layer.group_send)(
                self.consumer.room_group_name,
                {
                    'type': 'message_to_self',
                    'sender_channel_name': self.consumer.channel_name,
                    'message': f"{self.user} thinks: {thought_content}",
                }
            )
            return False
        else:
            return "What the hell are you thinking about?"

    def where(self):
        """Where é um comando muito massa!"""
        return f'{type(self.player.location_id)}: {self.player.location_id.__dict__}'

    def start(self):
        if self.player.level == 0:
            start_location = Location.objects.get(x_coord=0, y_coord=0, z_coord=0)
            self.player.move_to(start_location)
            self.player.level_up()
            return "You are at the center of the world now!"
        else:
            return "This is no longer a valid command"

    def north(self):
        dest_x = self.player.location_id.x_coord
        dest_y = self.player.location_id.y_coord + 1
        dest_z = self.player.location_id.z_coord
        dest_location = Location.objects.get(x_coord=dest_x, y_coord=dest_y, z_coord=dest_z)
        self.player.move_to(dest_location)
        return f'You move in the north direction'

    n = north

    def help(self):
        """If you use 'help' you can see a list of availlable commands.
        You can also use 'help <command>' to get a more specific guide."""
        methods_list = [func for func in dir(Engine) if callable(getattr(Engine, func)) and not func.startswith("__") and len(func) > 1]
        if len(self.command_line.split()) == 1:
            message = "This is the list of all commands available in this server:"
            for func in methods_list:
                message = message + f"\n{func!r}"
            return message
        elif len(self.command_line.split()) == 2:
            command_to_help = self.command_line.split(maxsplit=1)[1]
            if command_to_help in methods_list:
                help_text = eval('Engine.' + self.command_line.split(maxsplit=1)[1] +'.__doc__')
                return f"This is the 'help' for {command_to_help!r}: {help_text}"
            else:
                return f"{command_to_help!r} is not a valid command. We can't help you with that."
        else:
            return "Invalid input. You can either use 'help' or 'help <command>', but nothing more."

