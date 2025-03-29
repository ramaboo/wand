import time
import uasyncio as asyncio

from machine import ADC
from range import Range

from led import LED

class Steering(Range):
    HEARTBEAT = 5
    ADC_LOW = 2900
    ADC_HIGH = 7800
    
    def __init__(self):      
        self.left = 0
        self.left_raw = 0
        self.left_uv = 0

        self.left_adc = ADC(4)
        self.left_adc.atten(ADC.ATTN_11DB)

        self.right = 0
        self.right_raw = 0

        self.right_uv = 0
        self.right_adc = ADC(5)
        self.right_adc.atten(ADC.ATTN_11DB)
        
        self.direction = ('straight', 0)
    
    def setup(self, app):
        self.stepper = app.stepper
        self.stepper.enable()
        asyncio.create_task(self.read_action())
        asyncio.create_task(self.move_action())

    async def read_action(self):
        while True:
            self.read()
            #self.print()
            #self.print_direction()
                        
            await asyncio.sleep_ms(self.HEARTBEAT)

    async def move_action(self):
        while True:
            t_begin = time.ticks_ms()
        
            direction, speed = self.direction
                        
            if speed > 0:
                if direction == 'left':
                    self.stepper.enable()
                    self.stepper.left()
                    self.stepper.step()
                elif direction == 'right':
                    self.stepper.enable()
                    self.stepper.right()
                    self.stepper.step()
        
            sleep_time = ((100 - speed) // 2) + 1

            t_end = time.ticks_ms()
            t_delta = time.ticks_diff(t_end, t_begin)
                    
            await asyncio.sleep_ms(sleep_time - t_delta)

    def read(self):
        self.left_raw = self.left_adc.read()
        self.left = self.left_range()
        
        self.right_raw = self.right_adc.read()
        self.right = self.right_range()
        
        self.set_direction()


    def read_uv(self):
        self.left_uv = self.left_adc.read_uv()
        self.right_uv = self.right_adc.read_uv()

    def left_range(self):
        return self.map_range(self.left_raw, self.ADC_LOW, self.ADC_HIGH, 0, 100)

    def right_range(self):
        return self.map_range(self.right_raw, self.ADC_LOW, self.ADC_HIGH, 0, 100)
    
    def get_direction(self):
        if (self.left == 0 and self.right == 0):
            return ('straight', 0)
        
        if (self.left > 0 and self.right > 0):
            return ('error', 0)
    
        if (self.left > 0 and self.right == 0):
            return ('left', self.left)
        
        if (self.right > 0 and self.left == 0):
            return ('right', self.right)
        
        return ('exception', 0)
        
    def set_direction(self):
        self.direction = self.get_direction()
        return self.direction
        
    def print_all(self):
        self.read()
        self.read_uv()
        print('L: ', self.left, ' | L Raw: ', self.left_raw, ' | L uV: ', self.left_uv, '| R: ', self.right, ' | R Raw: ', self.right_raw, ' | R uV: ', self.right_uv)

    def print_raw(self):
        print('L Raw: ', self.left_raw, ' | R Raw: ', self.right_raw)
        
    def print(self):
        print('L: ', self.left, ' | R: ', self.right)
    
    def print_direction(self):
        print(self.direction)

    def print_loop(self):
        while True:
            self.print_all()
            time.sleep(1)
