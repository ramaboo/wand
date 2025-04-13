import time
import uasyncio as asyncio

class Timeout:
    HEARTBEAT = 1000
    
    CONTROL_INPUT_TIMEOUT = 5000
    
    def __init__(self):
        self.control_input = time.ticks_ms()
        
        
    def start(self, app):
        self.app = app
        asyncio.create_task(self.update_action())


    async def update_action(self):
        while True:
            now = time.ticks_ms()

            print(self.control_input)
            
            
            
            if time.ticks_diff(now, self.control_input) > self.CONTROL_INPUT_TIMEOUT:
                self.app.stepper.disable()
                                           
            await asyncio.sleep_ms(self.HEARTBEAT)
            
