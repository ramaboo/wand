import time
import uasyncio as asyncio

from machine import ADC, Timer
from range import Range
from rotary import RotaryIRQ

from led import LED

class RotarySteering(Range):
    R1_CLK = 38
    R1_DT = 39
    
    TIMER_ID = 0
    TIMER_FREQUENCY = 100
    
    def __init__(self):        
        self.rotary_position = 0
        
        self.stepper_position = 0
        
        self.r1 = RotaryIRQ(pin_num_clk=self.R1_DT, 
            pin_num_dt=self.R1_CLK, 
            min_val=0, 
            max_val=99,
            pull_up=True,
            reverse=False, 
            range_mode=RotaryIRQ.RANGE_UNBOUNDED)
        
        self.rotary_event = asyncio.Event()
        self.r1.add_listener(self.rotary_callback)
        
        self.timer = Timer(self.TIMER_ID)
    
    def start_timer(self):
        self.timer.deinit()
            
        self.timer.init(freq=self.TIMER_FREQUENCY, mode=Timer.PERIODIC, callback=self.timer_callback)
    
    def stop_timmer(self):
        self.timer.deinit()
    
    def timer_callback(self, t):
        if self.rotary_position == self.stepper_position:
            return
  
        if self.rotary_position > self.stepper_position:
            self.app.stepper.enable()
            self.app.stepper.right()
            self.app.stepper.safe_step()
            self.stepper_position += 1
            
        elif self.rotary_position < self.stepper_position:
            self.app.stepper.enable()
            self.app.stepper.left()
            self.app.stepper.safe_step()
            self.stepper_position -= 1

    def start(self, app):
        self.app = app
        self.app.stepper.enable()
        asyncio.create_task(self.rotary_action())
        
        self.start_timer()
  
    def rotary_callback(self):
        self.rotary_event.set()

    async def rotary_action(self):
        while True:
            await self.rotary_event.wait()
            
            self.rotary_position = self.r1.value()
            self.app.timeout.control_input = time.ticks_ms()
            
            self.rotary_event.clear()

