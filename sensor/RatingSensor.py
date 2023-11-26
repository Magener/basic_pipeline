import random
import asyncio
import websockets
import json

from sensor.CSVLoader import generator_from_csv

PORT = 8765
URL = "localhost"
RATINGS_FILE_PATH = './Ratings.csv'

async def broadcast_rating_data(websocket, path):
    for row in generator_from_csv(RATINGS_FILE_PATH):
        MIN_NEW_RATING_RATE = 0.5
        MAX_NEW_RATING_RATE = 2
        rating_rate = random.uniform(MIN_NEW_RATING_RATE, MAX_NEW_RATING_RATE)

        await websocket.send(json.dumps(row))
        await asyncio.sleep(rating_rate)

async def run_server():
    async with websockets.serve(broadcast_rating_data, URL, PORT):
        await asyncio.Future()



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run_server())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()