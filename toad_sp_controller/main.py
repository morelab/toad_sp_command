#!/usr/bin/env python3

import asyncio
from toad_sp_controller import config, command


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(command.main(config.MQTT_BROKER_HOST))
