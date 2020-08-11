import asyncio

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

from .models import Battle, Challenger


class BattleConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.battle_id = self.scope['url_route']['kwargs']['battle_id']
        self.battle_group_name = f'battle_{self.battle_id}'

        self.battle = await self.get_battle_object()
        self.battle_mode = False
        self.expecting_response = False
        self.decided = False

        await self.channel_layer.group_add(
            self.battle_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        if self.battle.state == Battle.WAITING:
            await self.del_disconnected_challenger()
        elif self.battle.state == Battle.READY:
            await self.del_disconnected_challenger()
            await self.channel_layer.group_send(
                self.battle_group_name, {
                    'type': 'battle.unready',
                }
            )
        elif self.battle.state == Battle.ACTIVE:
            pass

        await self.send_system_message(f'{self.challenger_name} has left.')

        await self.channel_layer.group_discard(
            self.battle_group_name,
            self.channel_name
        )

    async def receive_json(self, content):
        if content['type'] == 'challenger.join':
            self.challenger_name = content['username']
            await self.send_system_message(f'{self.challenger_name} has joined.')
            if self.battle.state == Battle.ACTIVE:
                self.expecting_response = True
                await self.channel_layer.group_send(
                    self.battle_group_name, {
                        'type': 'query.challenger_name',
                    }
                )
            else:
                if await self.update_status():
                    await self.send_system_message('Press the button to start!')
                    await self.channel_layer.group_send(
                        self.battle_group_name, {
                            'type': 'battle.ready',
                        }
                    )
        elif content['type'] == 'challenger.decide':
            self.decided = content['decision']
            await self.channel_layer.group_send(
                self.battle_group_name, content
            )
            if self.decided:
                await self.send_system_message(f'{self.challenger_name} is ready!')
        elif content['type'] == 'chat.message':
            if not self.battle_mode:
                await self.channel_layer.group_send(
                    self.battle_group_name, content
                )

    async def chat_message(self, event):
        await self.send_json(event)

    async def battle_ready(self, event):
        await self.send_json(event)

    async def battle_unready(self, event):
        await self.send_json(event)

    async def battle_activate(self, event):
        await self.send_json(event)

    async def battle_start(self, event):
        self.battle_mode = True
        await self.send_json(event)

    async def challenger_decide(self, event):
        if self.decided and event['username'] != self.challenger_name and event['decision']:
            await self.activate_battle()
            await self.channel_layer.group_send(
                self.battle_group_name, {
                    'type': 'battle.activate',
                }
            )
            await self.send_system_message(
                'Both users have confirmed that they want to start!'
            )
            await self.send_system_message('Starting in 10 seconds!')
            await asyncio.sleep(5)
            await self.send_system_message('Starting in 5 seconds!')
            await asyncio.sleep(2)
            await self.send_system_message('Starting in 3 seconds!')
            await asyncio.sleep(1)
            await self.send_system_message('Starting in 2 seconds!')
            await asyncio.sleep(1)
            await self.send_system_message('Starting in 1 second!')
            await asyncio.sleep(1)
            await self.channel_layer.group_send(
                self.battle_group_name, {
                    'type': 'battle.start',
                }
            )
            await self.send_system_message(
                'Chat has been disabled! Good luck, and may the best coder win!'
            )

    async def query_battle_mode(self, event):
        if event['username'] != self.challenger_name:
            await self.channel_layer.group_send(
                self.battle_group_name, {
                    'type': 'return.battle_mode',
                    'battle_mode': self.battle_mode
                }
            )

    async def return_battle_mode(self, event):
        if event['username'] != self.challenger_name and self.expecting_response:
            self.expecting_response = False
            if event['battle_mode']:
                await self.send_json({
                    'type': 'battle.activate'
                })
            else:
                await self.send_json({
                    'type': 'battle.start'
                })

    async def send_system_message(self, message):
        await self.channel_layer.group_send(
            self.battle_group_name, {
                'type': 'chat.message',
                'message': message,
                'sender': {'username': 'SYSTEM'},
            }
        )

    @database_sync_to_async
    def del_disconnected_challenger(self):
        Challenger.objects.get(user__username=self.challenger_name).delete()
        self.battle.state = Battle.WAITING
        self.battle.save()

    @database_sync_to_async
    def get_battle_object(self):
        return Battle.objects.get(pk=self.battle_id)

    @database_sync_to_async
    def update_status(self):
        ready = self.battle.challengers.count() == 2
        if ready:
            self.battle.state = Battle.READY
            self.battle.save()
        return ready

    @database_sync_to_async
    def activate_battle(self):
        self.battle.state = Battle.ACTIVE
        self.battle.save()
