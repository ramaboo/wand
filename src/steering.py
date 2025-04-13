import time
import uasyncio as asyncio

from machine import ADC, Timer
from range import Range

class Steering(Range):
    HEARTBEAT = 10
    
    LEFT_PIN = 4
    RIGHT_PIN = 5
    ADC_LOW = 2900
    ADC_HIGH = 7800
    
    TIMER_ID = 1
    TIMER_FREQUENCY = 100

    
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
        
        self.direction = 'straight'
        self.speed = 0
        
        self.timer = Timer(self.TIMER_ID)      
        
    def timer_callback(self, t):             
        if self.speed > 0:
            self.app.stepper.enable()
            if self.direction == 'left':
                self.app.stepper.left()
                
                for i in range(self.speed):
                    self.app.stepper.safe_step()
                    time.sleep_ms(1)
                
            elif self.direction == 'right':
                self.app.stepper.right()
                
                for i in range(self.speed):
                    self.app.stepper.safe_step()
                    time.sleep_ms(1)
                
        
    def start_timer(self):
        self.timer.deinit()
            
        self.timer.init(freq=self.TIMER_FREQUENCY, mode=Timer.PERIODIC, callback=self.timer_callback)
    
    def stop_timmer(self):
        self.timer.deinit()
                    
    def start(self, app):
        self.app = app
        self.app.stepper.enable()
        self.start_timer()
        asyncio.create_task(self.read_action())

    async def read_action(self):
        while True:
            self.read()
            #self.print()
            #self.print_direction()
                                           
            await asyncio.sleep_ms(self.HEARTBEAT)

    def read(self):
        self.left_raw = self.left_adc.read()
        self.left = self.left_range()
        
        self.right_raw = self.right_adc.read()
        self.right = self.right_range()
        
        self.set_direction_and_speed()

    def read_uv(self):
        self.left_uv = self.left_adc.read_uv()
        self.right_uv = self.right_adc.read_uv()

    def left_range(self):
        return self.map_range(self.left_raw, self.ADC_LOW, self.ADC_HIGH, 0, 3)

    def right_range(self):
        return self.map_range(self.right_raw, self.ADC_LOW, self.ADC_HIGH, 0, 3)
    
        
    def set_direction_and_speed(self):
        if (self.left == 0 and self.right == 0):
            self.direction = 'straight'
            self.speed = 0
            return
        
        if (self.left > 0 and self.right > 0):
            self.direction = 'error'
            self.speed = 0
            return
    
        if (self.left > 0 and self.right == 0):
            self.direction = 'left'
            self.speed = self.left
            self.app.timeout.control_input = time.ticks_ms()
            return
        
        if (self.right > 0 and self.left == 0):
            self.direction = 'right'
            self.speed =  self.right
            self.app.timeout.control_input = time.ticks_ms()
            return
        
        self.direction = 'exception'
        self.speed = 0
        
    def print_all(self):
        print('L: ', self.left, ' | L Raw: ', self.left_raw, ' | L uV: ', self.left_uv, '| R: ', self.right, ' | R Raw: ', self.right_raw, ' | R uV: ', self.right_uv)

    def print_raw(self):
        print('L Raw: ', self.left_raw, ' | R Raw: ', self.right_raw)
        
    def print(self):
        print('L: ', self.left, ' | R: ', self.right)
    
    def print_direction(self):
        print('D: ', self.direction, ' | S: ', self.speed)

    def print_loop(self):
        while True:
            self.read()
            self.read_uv()
            self.print_all()
            time.sleep(1)
