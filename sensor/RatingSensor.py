import os
import json
import random
import asyncio

import websockets
from functools import partial
from dotenv import load_dotenv
from sensor.CSVLoader import generator_from_csv
from sensor.log import logger


async def broadcast_rating_data(websocket, path, ratings_source_path):
    logger.info("User has been connected!")

    for row in generator_from_csv(ratings_source_path):
        MIN_NEW_RATING_RATE = 0.5
        MAX_NEW_RATING_RATE = 2
        rating_rate = random.uniform(MIN_NEW_RATING_RATE, MAX_NEW_RATING_RATE)

        await websocket.send(json.dumps(row))
        logger.info(f"Rating has been sent! {row}")
        await asyncio.sleep(rating_rate)


async def run_server():
    load_dotenv()
    async with websockets.serve(partial(broadcast_rating_data,
                                        ratings_source_path=os.getenv('RATINGS_FILE_PATH')),
                                os.getenv('URL'),
                                os.getenv('PORT')):
        await asyncio.Future()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run_server())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
