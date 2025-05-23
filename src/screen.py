import time
import sys
import uasyncio as asyncio
import qwiic_serlcd
from qwiic_i2c.micropython_i2c import MicroPythonI2C

from machine import I2C, Pin
from rotary import RotaryIRQ

from cycle import Cycle

class Screen:
    I2C_ADDRESS = 0x72
    I2C_SCL_PIN = 21
    I2C_SDA_PIN = 20
    
    NUM_ROWS = 4
    NUM_COLS = 20

    REFRESH = 5000
    
    R1_CLK = 35
    R1_DT = 36
    R1_SW = 37

    def __init__(self):
        i2c = MicroPythonI2C(scl=Pin(self.I2C_SCL_PIN), sda=Pin(self.I2C_SDA_PIN))
        self.lcd = qwiic_serlcd.QwiicSerlcd(address=self.I2C_ADDRESS, i2c_driver=i2c)

        self.r1 = RotaryIRQ(pin_num_clk=self.R1_DT, 
            pin_num_dt=self.R1_CLK, 
            min_val=0, 
            max_val=23,
            pull_up=True,
            reverse=False, 
            range_mode=RotaryIRQ.RANGE_UNBOUNDED)
        
        self.rotary_event = asyncio.Event()
        self.r1.add_listener(self.rotary_callback)
        
        self.current_value = 0
        self.last_value = 0
        
        self.screens = Cycle(['home', 'drive', 'wand', 'system'])       

    def start(self, app):
        self.app = app
        
        self.lcd.begin()

        self.render_screen()

        asyncio.create_task(self.rotary_action())
        asyncio.create_task(self.refresh_action())

    async def render_screen(self):
        current_item = self.screens.current_item()
        method = getattr(self, f'render_{current_item}')
        method()
       
    def render_home(self):
        #self.lcd.clear()
        self.lcd.setCursor(col=0, row=0)
        self.lcd.print('8-bit Bunny Home    ')
        
    def render_drive(self):
        #self.lcd.clear()
        self.lcd.setCursor(col=0, row=0)

        self.lcd.print('8-bit Bunny Drive   ')
        self.lcd.setCursor(col=0, row=1)
        rp = str(self.app.rotary_steering.rotary_position)
        self.lcd.print(f'RP: {rp}')
        
    def render_wand(self):
        #self.lcd.clear()
        self.lcd.setCursor(col=0, row=0)

        self.lcd.print('8-bit Bunny Wand     ')
        
    def render_system(self):
        #self.lcd.clear()
        self.lcd.setCursor(col=0, row=0)

        self.lcd.print('8-bit Bunny System  ')
        
    def rotary_callback(self):
        self.rotary_event.set()

    async def refresh_action(self):
        while True:
            t_begin = time.ticks_ms()

            self.render_screen()
            
            t_end = time.ticks_ms()
            t_delta = time.ticks_diff(t_end, t_begin)
            
            print(t_delta)
            
            await asyncio.sleep_ms(self.REFRESH)
            
    async def rotary_action(self):
        while True:
            await self.rotary_event.wait()
            print('R1: ', self.r1.value())

            self.last_value = self.current_value
            self.current_value = self.r1.value()
            
            if self.current_value > self.last_value:
                self.screens.next_item()
            elif self.current_value < self.last_value:
                self.screens.previous_item()
              
            self.render_screen()
  
            self.rotary_event.clear()




        