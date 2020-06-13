import asyncio
from json import dumps, loads, JSONDecodeError

from toad_sp_command import smartplug


class SmartPlugMock:
    """SmartPlugs will close the connection if the received command was
    incorrect or send a response if it was correct."""

    # correct command
    ok_command = {"system": {"set_relay_state": {"state": 1}}}
    # response sent by the mock to a correct command
    # TODO: correct response
    ok_response = {"system": {"set_relay_state": {"state": 1}}}

    def __init__(self, addr, port, loop: asyncio.AbstractEventLoop):
        self.addr = addr
        self.port = port
        self._coroutine = asyncio.start_server(
            SmartPlugMock.handle_command, self.addr, self.port, loop=loop,
        )
        self._loop = loop
        self.server: asyncio.base_events.Server = ...

    async def start(self):
        self.server = await self._loop.create_task(self._coroutine)

    async def stop(self):
        self.server.close()
        await self.server.wait_closed()

    @staticmethod
    async def handle_command(
        reader: asyncio.streams.StreamReader, writer: asyncio.streams.StreamWriter
    ) -> None:
        encrypted_cmd = await reader.read(2048)
        try:
            # decrypt and load message to raise exception if it is invalid
            cmd = loads(smartplug.decrypt(encrypted_cmd).decode("utf-8"))
            if cmd != SmartPlugMock.ok_command:
                raise smartplug.DecryptionException
            # send response
            response = dumps(SmartPlugMock.ok_response)
            encrypted_response = smartplug.encrypt(response.encode("utf-8"))
            writer.write(encrypted_response)
        except (JSONDecodeError, UnicodeDecodeError, smartplug.DecryptionException):
            # incorrect command, close connection
            pass
        writer.write_eof()
        await writer.drain()
        writer.close()
        await writer.wait_closed()
