import time
import uasyncio as asyncio

from machine import ADC
from range import Range

class Throttle(Range):
    HEARTBEAT = 100
    THROTTLE_PIN = 3
    ADC_LOW = 200
    ADC_HIGH = 8191
    
    def __init__(self):
        self.throttle = 0
        self.throttle_raw = 0
        self.throttle_uv = 0

        self.throttle_adc = ADC(self.THROTTLE_PIN)
        self.throttle_adc.atten(ADC.ATTN_11DB)     

    def start(self, app):
        self.app = app
        asyncio.create_task(self.read_action())

    async def read_action(self):
        while True:
            self.read()
            # self.print()
            self.app.segment.set_value(self.throttle)
            
            if self.throttle > 0:
                self.app.stepper.enable()
                self.app.timeout.control_input = time.ticks_ms()
            await asyncio.sleep_ms(self.HEARTBEAT)
    
    def read(self):
        self.throttle_raw = self.throttle_adc.read()
        self.throttle = self.throttle_range()
    
    def read_uv(self):
        self.throttle_uv = self.throttle_adc.read_uv()
    
    def throttle_range(self):
        return self.map_range(self.throttle_raw, self.ADC_LOW, self.ADC_HIGH, 0, 100)
    
    def print(self):
        print('T: ', self.throttle)
        
    def print_all(self):
        print('T: ', self.throttle, ' | T Raw: ', self.throttle_raw, ' | T uV ', self.throttle_uv)
            
    def print_loop(self):
        while True:
            self.read()
            self.read_uv()
            self.print_all()
            time.sleep_ms(500)   