from machine import Pin, Timer
import math
import time
import uasyncio as asyncio

class Stepper:
    STEP_PIN = 18
    DIRECTION_PIN = 17
    ENABLED_PIN = 16

    def __init__(
        self,
        step_pin=STEP_PIN,
        direction_pin=DIRECTION_PIN,
        enabled_pin=ENABLED_PIN
    ):

        self.step_pin = Pin(step_pin, Pin.OUT)
        self.direction_pin = Pin(direction_pin, Pin.OUT)
        self.enabled_pin = Pin(enabled_pin, Pin.OUT)
        
        self.last_direction = 'straight'
        self.enabled = False
                
  
    def step(self):
        self.step_pin.value(1)
        self.step_pin.value(0)           
        
    def left(self):
        if self.last_direction != 'left':
            self.direction_pin.value(0)
            self.last_direction = 'left'

    def right(self):
        if self.last_direction != 'right':
            self.direction_pin.value(1)
            self.last_direction = 'right'

    def enable(self):
        if self.enabled == True:
            return
        
        self.enabled_pin.value(0)
        self.enabled = True

    def disable(self):
        if self.enabled == False:
            return

        self.enabled_pin.value(1)
        self.enabled = False



