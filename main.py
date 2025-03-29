import time
import uasyncio as asyncio

from application import Application

HEARTBEAT = 100

async def main():
    app = Application()
    
    while True:
        await asyncio.sleep_ms(HEARTBEAT)

try:
   asyncio.run(main())
finally:
   asyncio.new_event_loop()
   
   
