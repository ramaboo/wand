from machine import Pin, Timer
import math
import time
import uasyncio as asyncio

class Stepper:
    STEP_PIN = 18
    DIRECTION_PIN = 15
    ENABLED_PIN = 16
    
    LEFT_LIMIT_PIN = 9
    RIGHT_LIMIT_PIN = 10

    def __init__(self):
        self.step_pin = Pin(self.STEP_PIN, Pin.OUT)
        self.direction_pin = Pin(self.DIRECTION_PIN, Pin.OUT)
        self.enabled_pin = Pin(self.ENABLED_PIN, Pin.OUT)

        self.left_limit_pin = Pin(self.LEFT_LIMIT_PIN, Pin.IN, Pin.PULL_UP)
        self.left_last_state = self.left_limit_pin.value()
        self.left_limit = not self.left_limit_pin.value()
        
        self.right_limit_pin = Pin(self.RIGHT_LIMIT_PIN, Pin.IN, Pin.PULL_UP)
        self.right_last_state = self.right_limit_pin.value()
        self.right_limit = not self.right_limit_pin.value()
        
        self.direction = 'straight'
        self.enabled = False
        
        
    def start(self):
        self.left_limit_pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.handle_left_interrupt)
        self.right_limit_pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.handle_right_interrupt)

    def handle_left_interrupt(self, t):        
        current_state = self.left_limit_pin.value()
        
        if current_state != self.left_last_state:     
            self.left_limit = (current_state == 0)
                            
            self.left_last_state = current_state

    def handle_right_interrupt(self, t):
        current_state = self.right_limit_pin.value()
        
        if current_state != self.right_last_state:     
            self.right_limit = (current_state == 0)
               
            self.right_last_state = current_state           
                           
    def step(self, count=1):
        for i in range(count):
            self.safe_step()
    
    def force_step(self):
        self.step_pin.value(1)
        self.step_pin.value(0) 

    def safe_step(self):        
        if (self.left_limit == True and self.direction == 'left') or (self.right_limit == True and self.direction == 'right'):
            return
        else:
            self.force_step()
        
    def left(self):
        if self.direction != 'left':
            self.direction_pin.value(0)
            self.direction = 'left'

    def right(self):
        if self.direction != 'right':
            self.direction_pin.value(1)
            self.direction = 'right'

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

    def print(self):
        print('L Limit: ', self.left_limit, ' | R Limit: ', self.right_limit, ' | Direction: ', self.direction)

