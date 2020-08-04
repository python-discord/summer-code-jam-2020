from django.conf import settings
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

from terminal.terminal_tools import colorize

from MUD.models import Room, Player


BANNER = """
           #####    ###    #####    ###      #     # #     # ######  
          #     #  #   #  #     #  #   #     ##   ## #     # #     # 
                # #     #       # #     #    # # # # #     # #     # 
           #####  #     #  #####  #     #    #  #  # #     # #     # 
          #       #     # #       #     #    #     # #     # #     # 
          #        #   #  #        #   #     #     # #     # #     # 
          #######   ###   #######   ###      #     #  #####  ######  

                          Welcome to == 2020 MUD ==
                          Where the future is NOW.
                          Type "help" for a list of commands
""".replace('\n', '\r\n')


class MudConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            # Accept the connection
            await self.accept()
            await self.join_room()
            await self.send_welcome()

    async def receive_json(self, content):
        command = content.get("command", None)
        try:
            if command == "leave":
                await self.leave_room()
            elif command == "send":
                await self.send_room(content["message"])
            elif command == "help":
                await self.send_help()
            elif command == "look":
                await self.send_room_description()
            else:
                await self.send_unknown(command)
        except Exception as e:
            await self.send_json({"error": e})

    async def disconnect(self, code):
        try:
            await self.leave_group()
        except Exception:
            pass

    async def send_welcome(self):
        await self.send_json( {'message': colorize('brightBlue', BANNER)} )

    async def send_unknown(self, command):
        await self.send_json({
            'message': f"I don't understand `{command}`, try " + colorize('brightYellow', "help") + "."
        })

    async def send_help(self):
        await self.send_json({
            'message': 'options: help, send, leave, look' # we should have a set() of commands/options
        })

    async def send_room_description(self):
        message = await self.get_current_room_description()
        await self.send_json({
            'message': message
        })

    @database_sync_to_async
    def get_current_room_description(self):
        """ Returns a string with the description of the current room.  """

        try:
            player = Player.objects.get(user=self.scope["user"])
        except Player.DoesNotExist:
            return "Current user does not have a Player!"

        room_name = colorize('brightGreen', player.room.name)
        description = player.room.description

        # TODO this can likely be cleaned up a bit
        exits = list(player.room.connections.all())
        exit_names = []
        for exit in exits:
            exit_names.append(colorize('brightGreen', exit.name))
        exits_string = ", ".join(exit_names)

        message = "You are in " + room_name + "\r\n\n" + description + "\r\n\nExits: " + exits_string
        return message

    @database_sync_to_async
    def move_to_room(self):
        pass

    async def join_room(self):
        if not self.scope['user'].is_authenticated:
            pass
        await self.channel_layer.group_send(
            'dungeon',
            {
                'type': 'chat.join',
                'username': self.scope['user'].username,
            }
        )
        self.isOnline = True
        await self.channel_layer.group_add(
            'dungeon',
            self.channel_name,
        )
        await self.send_json({
            "join": str('dungeon'),
            "title": 'dungeon',
        })

    async def leave_room(self):
        await self.channel_layer.group_send(
            'dungeon',
            {
                'type': 'dungeon.leave',
                'username': self.scope['user'].username,
            }
        )
        self.isOnline = False
        await self.channel_layer.group_discard(
            'dungeon',
            self.channel_name,
        )
        await self.send_json({
            "leave": str('dungeon'),
        })

    async def send_room(self, message):
        if not self.isOnline:
            raise Exception('Rejected')
        await self.channel_layer.group_send(
            'dungeon',
            {
                "type": "chat.message",
                "username": self.scope["user"].username,
                "message": message,
            }
        )

    # These helper methods are named by the types we send - so chat.join becomes chat_join
    async def chat_join(self, event):
        await self.send_json(
            {
                "msg_type": 'ENTER',
                "username": event["username"],
            },
        )

    async def chat_leave(self, event):
        """
        Called when someone has left our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                "msg_type": 'EXIT',
                "username": event["username"],
            },
        )

    async def chat_message(self, event):
        """
        Called when someone has messaged our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                "msg_type": event['type'],
                "username": event["username"],
                "message": event["message"],
            },
        )
