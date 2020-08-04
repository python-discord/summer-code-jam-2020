import asyncio
from asyncio.exceptions import CancelledError
from typing import Optional
from asyncio import subprocess
from asyncio.streams import StreamReader

from channels.generic.websocket import AsyncWebsocketConsumer


# TODO: add auth (check self.scope for user)
class TerminalConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        await self.accept()
        self.process = await subprocess.create_subprocess_shell(
            '../build/process_watch bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.task_err = asyncio.tasks.create_task(
            self.handle_sending(self.process.stderr))
        self.task_out = asyncio.tasks.create_task(
            self.handle_sending(self.process.stdout))

    async def disconnect(self, code: Optional[int]) -> None:
        self.process.terminate()
        self.task_err.cancel()
        self.task_out.cancel()

    async def handle_sending(self, stream: StreamReader) -> None:
        print('starting', stream)
        try:
            while True:
                to_send = await stream.read(256)
                if to_send:
                    await self.send(bytes_data=to_send)
        except CancelledError:
            pass

    async def receive(self, text_data: str = None, bytes_data: bytes = None) -> None:
        self.process.stdin.write(text_data.encode())
