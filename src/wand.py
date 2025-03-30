import time
import uasyncio as asyncio

from machine import ADC, Pin
from range import Range

class Wand(Range):
    HEARTBEAT = 50

    LEFT_PIN = 8
    RIGHT_PIN = 19 # Not used yet!
    ADC_LOW = 150
    ADC_HIGH = 8191
    
    def __init__(self):
        self.left = 0
        self.left_raw = 0
        self.left_uv = 0
        
        self.left_adc = ADC(self.LEFT_PIN)
        self.left_adc.atten(ADC.ATTN_11DB)
        
        self.right = 0
        self.right_raw = 0

        self.right_uv = 0
        self.right_adc = ADC(self.RIGHT_PIN)
        self.right_adc.atten(ADC.ATTN_11DB)
        
    def start(self, app):
        self.app = app
        asyncio.create_task(self.read_action())
        
        
    async def read_action(self):
        while True:
            self.read()
            self.print()
                        
            await asyncio.sleep_ms(self.HEARTBEAT)
            
    def read(self):
        self.left_raw = self.left_adc.read()
        self.left = self.left_range()
        
        self.right_raw = self.right_adc.read()
        self.right = self.right_range()
        
    def read_uv(self):
        self.left_uv = self.left_adc.read_uv()
        self.right_uv = self.right_adc.read_uv()

    def left_range(self):
        return self.map_range(self.left_raw, self.ADC_LOW, self.ADC_HIGH, 0, 100)

    def right_range(self):
        return self.map_range(self.right_raw, self.ADC_LOW, self.ADC_HIGH, 0, 100)
    
    def print_all(self):
        print('L: ', self.left, ' | L Raw: ', self.left_raw, ' | L uV: ', self.left_uv, '| R: ', self.right, ' | R Raw: ', self.right_raw, ' | R uV: ', self.right_uv)

    def print_raw(self):
        print('L Raw: ', self.left_raw, ' | R Raw: ', self.right_raw)
        
    def print(self):
        print('L: ', self.left, ' | R: ', self.right)
    
    def print_direction(self):
        print(self.direction)

    def print_loop(self):
        while True:
            self.read()
            self.read_uv()
            self.print_all()
            time.sleep(1)
