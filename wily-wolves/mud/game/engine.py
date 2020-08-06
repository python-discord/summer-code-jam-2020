from asgiref.sync import async_to_sync
from game.models import Player

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
