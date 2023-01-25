import websockets
import asyncio


async def handler(websocket, path):
    data = await websocket.recv()
    print(f"received data: {data}")
    reply = f"hello from web socket server. Address: Arcadia Terrace 611"
    await websocket.send(reply)


start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
