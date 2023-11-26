import json
import asyncio
import websockets

from receiver.consts import SENSOR_URL
from receiver.log import logger



async def listen_for_new_ratings():
    async with websockets.connect(SENSOR_URL) as websocket:
        logger.info(f'Connected to {SENSOR_URL}')
        while True:
            rating_data = json.loads(await websocket.recv())

            logger.info(f"Rating data has been received: {rating_data}")


asyncio.run(listen_for_new_ratings())
