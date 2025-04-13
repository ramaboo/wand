
import uasyncio as asyncio

from stepper import Stepper
from steering import Steering

class Application():
    def __init__(self):
        self.stepper = Stepper()        
        
    def start(self):
        self.stepper.start()



HEARTBEAT = 100

async def main():
    app = Application()
    app.start()


    s = Steering()
    s.start(app)

    while True:
        await asyncio.sleep_ms(HEARTBEAT)


asyncio.run(main())