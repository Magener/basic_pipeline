import json
import asyncio
import websockets
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SENSOR_URL = "ws://localhost:8765"

async def listen_for_new_ratings():
    async with websockets.connect(SENSOR_URL) as websocket:
        logger.info(f'Connected to {SENSOR_URL}')
        while True:
            rating_data = json.loads(await websocket.recv())

            logger.info(f"Rating data has been received: {rating_data}")

asyncio.run(listen_for_new_ratings())