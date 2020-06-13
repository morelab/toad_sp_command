import pytest

from tests import mocks
from toad_sp_command import smartplug


@pytest.fixture
async def smartplug_mock(unused_tcp_port, event_loop) -> mocks.SmartPlugMock:
    sp_mock = mocks.SmartPlugMock("127.0.0.1", unused_tcp_port, event_loop)
    await sp_mock.start()
    yield sp_mock
    await sp_mock.stop()


@pytest.mark.asyncio
async def test_get_power(smartplug_mock):
    ok, response = await smartplug.set_status(
        True, smartplug_mock.addr, smartplug_mock.port
    )
    assert ok and type(response) is dict and response == mocks.SmartPlugMock.ok_response
    ok, _ = await smartplug.set_status(False, "0.0.0.0", 0)
    assert not ok
