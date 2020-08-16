import asyncio
from operator import itemgetter
from asyncio.exceptions import CancelledError
from typing import Literal, Optional, Union
from asyncio import subprocess
from asgiref.sync import sync_to_async
from asyncio.streams import StreamReader
from vmachine.models import VMachine, Floppy
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from the_htvms.runner.vm import start_vm
from the_htvms.runner.config import VMConfig
from channels.generic.websocket import AsyncWebsocketConsumer


# TODO: add auth (check self.scope for user)
class TerminalConsumer(AsyncWebsocketConsumer):
    @sync_to_async
    def _check_user(self, user: User, storage_id: int, vm_id: int) -> Union[Literal[False], str]:
        """
        return False if the user can use the given storage and vm, otherwise a non-empty error message
        """
        try:
            virtual_machine = VMachine.objects.get(pk=vm_id)
        except ObjectDoesNotExist:
            return "Virtual Machine not found"
        else:
            if virtual_machine.user != user:
                return "That's not your VirtualMachine!"
            else:
                try:
                    floppy = Floppy.objects.get(storage_id=storage_id)
                except ObjectDoesNotExist:
                    return "Floppy not found"
                else:
                    if floppy.user != user:
                        return "That's not your Floppy!"
                    else:
                        return False

    @sync_to_async
    def _create_vmcfg(self, storage_id: int, vm_id: int):
        user = self.scope.get('user')
        vm = VMachine.objects.get(id=vm_id)
        return VMConfig('bash', vm.floppy_disks_id)

    async def connect(self) -> None:
        await self.accept()
        storage_id, vm_id = itemgetter('storage_id', 'vm_id')(self.scope['url_route']['kwargs'])
        user = self.scope.get('user')
        error = 'invalid user'
        self.connected = False
        if user is None or not user.is_authenticated or (error := await self._check_user(user, storage_id, vm_id)):
            print('errored', error)
            # sending text would require special handling on the client side
            await self.send(bytes_data=(error + '\n').encode())
            await self.close()
            return
        self.connected = True
        self.vmcfg = await self._create_vmcfg(storage_id, vm_id)
        self.process = await subprocess.create_subprocess_exec(
            *start_vm(self.vmcfg), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.task_err = asyncio.tasks.create_task(
            self.handle_sending(self.process.stderr))
        self.task_out = asyncio.tasks.create_task(
            self.handle_sending(self.process.stdout))

    async def disconnect(self, code: Optional[int]) -> None:
        if self.connected:
            self.process.terminate()
            self.task_err.cancel()
            self.task_out.cancel()

    async def handle_sending(self, stream: StreamReader) -> None:
        try:
            while True:
                to_send = await stream.read(256)
                if to_send:
                    await self.send(bytes_data=to_send)
        except CancelledError:
            pass

    async def receive(self, text_data: str = None, bytes_data: bytes = None) -> None:
        self.process.stdin.write(text_data.encode())
