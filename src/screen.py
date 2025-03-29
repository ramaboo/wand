import uasyncio as asyncio

from machine import I2C, Pin
from lcd_i2c import LCD
from rotary import RotaryIRQ

class Screen:
    I2C_ADDRESS = 0x27
    I2C_SCL_PIN = 13
    I2C_SDA_PIN = 12
    NUM_ROWS = 4
    NUM_COLS = 20
    LCD_FREQUENCY = 800000
    
    R1_CLK = 35
    R1_DT = 36
    R1_SW = 37

    def __init__(self):        
        i2c = I2C(0, scl=Pin(self.I2C_SCL_PIN), sda=Pin(self.I2C_SDA_PIN), freq=self.LCD_FREQUENCY)
        self.lcd = LCD(addr=self.I2C_ADDRESS, cols=self.NUM_COLS, rows=self.NUM_ROWS, i2c=i2c)

        self.lcd.begin()
        self.lcd.print('8-bit Bunny')

        self.r1 = RotaryIRQ(pin_num_clk=self.R1_DT, 
            pin_num_dt=self.R1_CLK, 
            min_val=0, 
            max_val=23,
            pull_up=True,
            reverse=False, 
            range_mode=RotaryIRQ.RANGE_WRAP)
        
        self.rotary_event = asyncio.Event()
        self.r1.add_listener(self.rotary_callback)
        asyncio.create_task(self.action())


    def rotary_callback(self):
        self.rotary_event.set()

    async def action(self):
        while True:
            await self.rotary_event.wait()
            print('R1: ', self.r1.value())
            # do something with the encoder result ...

            
            self.rotary_event.clear()




