import json
import asyncio
import websockets
import os
from dotenv import load_dotenv

from receiver.log import logger

load_dotenv()


async def listen_for_new_ratings():
    async with websockets.connect(SENSOR_URL) as websocket:
        logger.info(f'Connected to {SENSOR_URL}')
        while True:
            rating_data = json.loads(await websocket.recv())

            logger.info(f"Rating data has been received: {rating_data}")


SENSOR_URL = os.getenv('SENSOR_URL')
asyncio.run(listen_for_new_ratings())
