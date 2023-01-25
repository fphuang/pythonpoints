import asyncio
import websockets


async def test():
    async with websockets.connect('ws://localhost:8000') as websocket:
        for k in range(10):
            await websocket.send(f"hello from python client: {k}")
            response = await websocket.recv()
            print(response)

asyncio.get_event_loop().run_until_complete(test())
