#!/usr/bin/env python

import asyncio
import datetime
import websockets

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await asyncio.sleep(1)
        await websocket.send(now)

async def main():
    async with websockets.serve(time, "localhost", 8000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
