import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            response = await websocket.recv()
            print(f"Received from server: {response}")

asyncio.run(hello())