import asyncio
import websockets

async def echo(websocket, path):
    while True:
        message = "Periodic message from server"
        await websocket.send(message)
        await asyncio.sleep(1)

async def run_server():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # To keep the server running indefinitely

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run_server())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()