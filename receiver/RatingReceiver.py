import json
import asyncio
import websockets


async def listen_for_new_ratings():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            rating_data = json.loads(await websocket.recv())

            print(f"Rating data has been received: {rating_data}")

asyncio.run(listen_for_new_ratings())